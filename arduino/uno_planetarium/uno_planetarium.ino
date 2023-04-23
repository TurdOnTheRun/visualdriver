#include <Light.h>
#include <LightSetting.h>
#include <LightEffect.h>
#include <SerialInterpreter.h>
#include <PWM.h>


class UnoLight: public Light {
  private:
    int32_t _frequency = 31000; //frequency (in Hz)
    
  public:
    UnoLight(byte id, byte pin, LightSetting* setting):Light(id, pin, setting){};
    void set_pin_frequency() {
      //sets the frequency for the specified pin
      SetPinFrequencySafe(_pin, _frequency);
    };
    void pin_write() {
      pwmWrite(_pin, _statemap[_newstate]);
    }
};


// Derived class
class Motor {
  protected:
    const byte RPWM_pin = 5;
    const byte LPWM_pin = 6;
    byte OUT_pin;
    byte NOTOUT_pin;
    const byte MAXIMAL_SPEED_DIFFERENCE = 5;
    const byte MAXIMUM_SPEED = 130;
    boolean stopped = true;
    boolean changingDirection = false;
    byte state;
    byte tostate;
    byte savestate;
    byte steptime;
    unsigned long laststep;

  public:

    Motor(){}
    
    void init() {
      pinMode(RPWM_pin, OUTPUT);
      pinMode(LPWM_pin, OUTPUT);
      OUT_pin = LPWM_pin;
      NOTOUT_pin = RPWM_pin;
    }

    void update() {
      
      if (changing()){
        
        unsigned long passed = millis() - laststep;
        int steps;
        
        if (passed < steptime){
          return;
        } else {
          steps = (int) round(passed/steptime);
        }

        int newstate;
        
        if (rising()){
          
          newstate = ((int)state)+steps;
          
          if (newstate >= tostate || newstate > 255){
            setstate(tostate);
          } else {
            setstate(lowByte(newstate));
          }
          
        } else {
          
          newstate = ((int)state)-steps;
          
          if (newstate <= tostate || newstate < 0){
            setstate(tostate);
          } else {
            setstate(lowByte(newstate));
          }
          
        }
      } else if (changingDirection && stopped) {
        byte TEMP_pin = OUT_pin;
        OUT_pin = NOTOUT_pin;
        NOTOUT_pin = TEMP_pin;
        changingDirection = false;
        setto(savestate,20);
      }
    }

    void setstate(byte newstate) {
      analogWrite(NOTOUT_pin,0);
      analogWrite(OUT_pin,newstate);
      if (newstate != 0){
        stopped = false;
      } else {
        stopped = true;
      }
      laststep = millis();
      state = newstate;
    }

    void setto(byte state_in, byte steptime_in) {
      if (changingDirection){
        return;
      }
      if (steptime_in < 20) {
        byte difference;
        if (state > state_in) {
          difference = state-state_in;
        } else {
          difference = state_in-state;
        }
        if (difference > MAXIMAL_SPEED_DIFFERENCE){
          steptime_in = 20;
        }
      }
      if (state_in > MAXIMUM_SPEED){
        state_in = MAXIMUM_SPEED;
      }
      tostate = state_in;
      steptime = steptime_in;
      laststep = millis();
    }

    void changedirection() {
      savestate = state;
      tostate = 0;
      steptime = 20;
      changingDirection = true;
    }

    bool rising() {
      return (state < tostate);
    }

    bool changing() {
      return !(state == tostate);
    }

};

Motor motor = Motor();

// ARDUINO SPECIFIC
//Available Pins:
//3,9,10
const byte light1 = 3;
const byte light2 = 9;
const byte light3 = 10;

// ARDUINO SPECIFIC
const byte numberOfLights = 3;
const byte numberOfSettings = 4;
const byte numberOfEffects = (numberOfLights * EFFECTSPERLIGHT) + 1;

// ARDUINO SPECIFIC
// Always must be one more than numberOfLights
LightSetting lightSettings[numberOfSettings] = {
  LightSetting(STATICMACHINE,60,0,100,50,3,0,0,0),
  LightSetting(),
  LightSetting(),
  LightSetting(),
};

LightEffect lightEffects[numberOfEffects];

// ARDUINO SPECIFIC
UnoLight lights[numberOfLights] = {
  Light(0, light1, &lightSettings[0]),
  Light(1, light2, &lightSettings[0]),
  Light(2, light3, &lightSettings[0]),
};

SerialInterpreter interpreter = SerialInterpreter();
unsigned long now;

// One message consists of a maximum of 10 bytes
byte type; //id of setting or effect
byte targetlights; //bit map for what lights the effect is for
// settings
byte set1;
byte set2;
byte set3;
byte set4;
byte set5;
byte set6;
byte set7;
byte set8;


void set_setting(byte targetlights, LightSetting setting){

  byte i;

  // Write setting into array
  for(i=0; i < numberOfSettings; i++) {
    if(lightSettings[i].is_unused()){
      lightSettings[i] = setting;
      lightSettings[i].init(now);
      break;
    }
  };

  for(byte j = 0; j < numberOfLights; j++) {
    if(bitRead(targetlights, j)){
      lights[j].set_setting(&lightSettings[i]);
    }
  };
}


void add_effect(byte targetlights, LightEffect effect){

  byte i;

  // Write setting into array
  for(i=0; i < numberOfEffects; i++) {
    if(lightEffects[i].is_unused()){
      lightEffects[i] = effect;
      lightEffects[i].init(now);
      break;
    }
  };

  for(byte j=0; j < numberOfLights; j++) {
    if(bitRead(targetlights, j)){
      lights[j].add_effect(&lightEffects[i]);
    }
  };
}

void reset_effects(byte targetlights){
  for(byte j=0; j < numberOfLights; j++) {
    if(bitRead(targetlights, j)){
      lights[j].remove_effects();
    }
  };
}

void remove_effect(byte targetlights, byte effectindex){
  for(byte j=0; j < numberOfLights; j++) {
    if(bitRead(targetlights, j)){
      lights[j].remove_effect(effectindex);
    }
  };
}


void parse_data() {
  // split the data into its parts

  type = 0; //id of setting or effect
  targetlights = 0; //bit map for what lights the effect is for
  // Setting Variables
  set1 = 0;
  set2 = 0;
  set3 = 0;
  set4 = 0;
  set5 = 0;
  set6 = 0;
  set7 = 0;
  set8 = 0;

  LightSetting setting;
  LightSetting effect;

  type = interpreter.inputBuffer[0];
  targetlights = interpreter.inputBuffer[1];

  // ARDUINO SPECIFIC
  // Handles Motor Commands
  if (type == 220) {
    // set1: state
    // set2: steptime
    set1 = interpreter.inputBuffer[1];
    set2 = interpreter.inputBuffer[2];
    motor.setto(set1,set2);
    return;
  } else if (type == 221) {
    motor.changedirection();
    return;
  }

  switch(type){
    case STATICLIGHT: {
      //set1: state 
      set1 = interpreter.inputBuffer[2];
    } break;

    case STATICFLASH: {
      //set1: start state
      //set2: to state
      //set3: flash time
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
    } break;

    case STATICMACHINE: {
      //set1: on state
      //set2: off state
      //set3: on time
      //set4: off time
      //set5: amount of times 
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
      set4 = interpreter.inputBuffer[5];
      set5 = interpreter.inputBuffer[6];
    } break;

    case LINEARDIMM: {
      //set1: start state
      //set2: to state
      //set3: steptime
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
    } break;

    case BEZIERDIMM: {
      //set1: start state
      //set2: to state
      //set3: steptime
      //set4: y1 of bezier input
      //set5: y2 of bezier input
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
      set4 = interpreter.inputBuffer[5];
      set5 = interpreter.inputBuffer[6];
    } break;

    case UPVIBRATO: 
    case DOWNVIBRATO:
    case UPDOWNVIBRATO: {
      //set1: amplitude
      //set2: steptime
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
    } break;

    case STROBE: {
      //set1: amplitude
      //set2: steptime
      //set3: steptime factor
      //set4: multisetting
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
      set4 = interpreter.inputBuffer[5];
    } break;

    case RESETEFFECTS: {
      //only needs target lights
      reset_effects(targetlights);
      return;
    } break;

    case REMOVEEFFECT: {
      //set1: effect index
      set1 = interpreter.inputBuffer[2];
      remove_effect(targetlights, set1);
      return;
    } break;

    default: {
      return;
    } break;
  }

  // Settings
  if(type < 100){
    set_setting(targetlights, LightSetting(type, set1, set2, set3, set4, set5, set6, set7, set8));
  } 
  else if(type < 200){
    add_effect(targetlights, LightEffect(type, set1, set2, set3, set4, set5, set6, set7, set8));
  }
}

void lights_setup() {
  for(byte i = 0; i < numberOfLights; i++) {
    lights[i].init();
  };
}

void settings_setup() {
  lightSettings[0].init(now);
}

void update_lights() {
  now = millis();
  for(byte i = 0; i < numberOfLights; i++) {
    lights[i].update(now);
  };
}

void read_serial() {
  // receive data from Python and save it into interpreter.inputBuffer
  while(Serial1.available() > 0) {
    
    byte x = Serial1.read();
    bool isEnd = interpreter.processByte(x);
    
    if(isEnd){
      parse_data();
    }
    
  }
}

void setup() {
  // ARDUINO SPECIFIC
  Serial.begin(115200);
  InitTimersSafe();
  motor.init(); 

  lights_setup();
  now = millis();
  settings_setup();
  update_lights();
}

void loop() {
  read_serial();
  update_lights();
  // ARDUINO SPECIFIC
  motor.update();
}
