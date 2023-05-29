#include <Light.h>
#include <Effect.h>
#include <Channel.h>
#include <Setting.h>
#include <Controlls.h>
#include <SerialInterpreter.h>
#include <PWM.h>


class UnoLight: public Light {
  private:
    int32_t _frequency = 31000; //frequency (in Hz)
    void set_pin_frequency() {
      //sets the frequency for the specified pin
      SetPinFrequencySafe(_pin, _frequency);
    };
    void pin_write() {
      pwmWrite(_pin, _statemap[_newstate]);
    }
    
  public:
    UnoLight(byte id, byte pin, Channel* channel):Light(id, pin, channel){};

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
const byte light1 = 9;
const byte light2 = 10;
//const byte light3 = 3;

// ARDUINO SPECIFIC
const byte numberOfLights = 2;

const byte numberOfSettings = 4;
const byte numberOfEffects = 8;
const byte numberOfChannels = 21;

// ARDUINO SPECIFIC
Setting settings[numberOfSettings] = {
  Setting(),
  Setting(),
  Setting(),
  Setting(),
};

Effect effects[numberOfEffects];

Channel channels[numberOfChannels] = {
  Channel(0),
  Channel(10),
  Channel(20),
  Channel(30),
  Channel(40),
  Channel(50),
  Channel(60),
  Channel(70),
  Channel(80),
  Channel(90),
  Channel(100),
  Channel(),
  Channel(),
  Channel(),
  Channel(),
  Channel(),
  Channel(),
  Channel(),
  Channel(),
  Channel(),
  Channel(),
};


// ARDUINO SPECIFIC
UnoLight lights[numberOfLights] = {
  UnoLight(0, light1, &channels[3]),
  UnoLight(1, light2, &channels[3]),
};

SerialInterpreter interpreter = SerialInterpreter();
unsigned long now;

// One message consists of a maximum of 10 bytes
byte type; //id of setting or effect
byte target; //bit map for what lights the effect is for
// settings
byte set1;
byte set2;
byte set3;
byte set4;
byte set5;
byte set6;
byte set7;
byte set8;


void setting_add(byte index, Setting setting){
  if(index < numberOfSettings){
    settings[index] = setting;
  }
}


void effect_add(byte index, Effect effect){
  if(index < numberOfEffects){
    effects[index] = effect;
  }
}

void light_set_channel(byte index, byte targetlights){
  for(byte j=0; j < numberOfLights; j++) {
    if(bitRead(targetlights, j)){
      lights[j].set_channel(&channels[index]);
    }
  };
}


void channel_set_setting(byte channelindex, byte settingindex){
  if(channelindex < numberOfChannels && settingindex < numberOfSettings){
    channels[channelindex].set_setting(&settings[settingindex]);
    channels[channelindex].set_channel(nullptr);
  }
}


void channel_set_channel(byte channelindex, byte inputchannelindex){
  if(channelindex < numberOfChannels && inputchannelindex < numberOfChannels){
    channels[channelindex].set_channel(&channels[inputchannelindex]);
    channels[channelindex].set_setting(nullptr);
  }
}


void channel_add_effect(byte channelindex, byte effectindex, byte channeleffectindex){
  if(channelindex < numberOfChannels && effectindex < numberOfEffects && channeleffectindex < EFFECTSPERCHANNEL){
    channels[channelindex].add_effect(&effects[effectindex], channeleffectindex);
  }
}


void channel_remove_effect(byte channelindex, byte effectindex){
  if(channelindex < numberOfChannels && effectindex < EFFECTSPERCHANNEL){
    channels[channelindex].remove_effect(effectindex);
  }
}

void channel_remove_effects(byte index){
  if(index < numberOfChannels){
    channels[index].remove_effects();
  }
}

void channels_reset(){
  //starts at 11 to preserve the static channels
  for(byte i = 11; i < numberOfChannels; i++) {
    channels[i] = Channel();
  };
}

void settings_reset(){
  for(byte i = 0; i < numberOfSettings; i++) {
    settings[i] = Setting();
  };
}

void effects_reset(){
  for(byte i = 0; i < numberOfEffects; i++) {
    effects[i] = Effect();
  };
}

void parse_data() {
  // split the data into its parts

  type = 0; //id of setting or effect
  target = 0; //bit map for what lights the effect is for
  // Setting Variables
  set1 = 0;
  set2 = 0;
  set3 = 0;
  set4 = 0;
  set5 = 0;
  set6 = 0;
  set7 = 0;
  set8 = 0;

  Setting setting;
  Setting effect;

  type = interpreter.inputBuffer[0];
  target = interpreter.inputBuffer[1];

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
    case SETTING_STATICLIGHT: {
      //set1: state 
      set1 = interpreter.inputBuffer[2];
    } break;

    case SETTING_STATICFLASH: {
      //set1: start state
      //set2: to state
      //set3: flash time
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
    } break;

    case SETTING_STATICMACHINE: {
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

    case SETTING_LINEARDIMM: {
      //set1: start state
      //set2: to state
      //set3: steptime
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
    } break;

    case SETTING_BEZIERDIMM: {
      //set1: start state
      //set2: to state
      //set3: steptime
      //set4: decisteps
      //set5: y1 of bezier input
      //set6: y2 of bezier input
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
      set4 = interpreter.inputBuffer[5];
      set5 = interpreter.inputBuffer[6];
      set6 = interpreter.inputBuffer[7];
    } break;

    case EFFECT_UPVIBRATO: 
    case EFFECT_DOWNVIBRATO:
    case EFFECT_UPDOWNVIBRATO: {
      //set1: amplitude channel index
      //set2: steptime channel index
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
    } break;

    case EFFECT_STROBE: {
      //set1: amplitude channel index
      //set2: steptime channel index
      //set3: steptime factor
      //set4: multisetting
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
      set4 = interpreter.inputBuffer[5];
    } break;

    case EFFECT_PERLIN: {
      //set1: amplitude channel index
      //set2: steptime channel index
      //set3: steptime factor
      //set4: multisetting
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
      set4 = interpreter.inputBuffer[5];
    } break;

    case LIGHT_SET_CHANNEL: {
      //set1: channelindex
      set1 = interpreter.inputBuffer[2];
      light_set_channel(set1, target);
      return;
    } break;

    case CHANNEL_SET_SETTING: {
      //set1: settingindex
      set1 = interpreter.inputBuffer[2];
      channel_set_setting(target, set1);
      return;
    } break;

    case CHANNEL_SET_CHANNEL: {
      //set1: channelindex
      set1 = interpreter.inputBuffer[2];
      channel_set_channel(target, set1);
      return;
    } break;

    case CHANNEL_ADD_EFFECT: {
      //set1: effectindex
      //set2: channeleffectindex
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      channel_add_effect(target,set1,set2);
      return;
    } break;

    case CHANNEL_REMOVE_EFFECT: {
      //set1: effectindex
      set1 = interpreter.inputBuffer[2];
      channel_remove_effect(target, set1);
      return;
    } break;

    case CHANNEL_REMOVE_EFFECTS: {
      channel_remove_effects(target);
      return;
    } break;

    case SETTINGS_RESET: {
      settings_reset();
      return;
    } break;

    case EFFECTS_RESET: {
      effects_reset();
      return;
    } break;

    case CHANNELS_RESET: {
      channels_reset();
      return;
    } break;

    default: {
      return;
    } break;
  }

  // Settings
  if(type < 60){
    setting_add(target, Setting(type, set1, set2, set3, set4, set5, set6, set7, set8));
  } 
  else if(type < 150){
    if(set1 < numberOfChannels && set2 < numberOfChannels){
      effect_add(target, Effect(type, &channels[set1], &channels[set2], set3, set4, set5, set6, set7, set8));
    }
  }
}

void lights_setup() {
  for(byte i = 0; i < numberOfLights; i++) {
    lights[i].init();
  };
}

void update_lights() {
  now = millis();
  for(byte i = 0; i < numberOfLights; i++) {
    lights[i].update(now);
  };
}

void read_serial() {
  // receive data from Python and save it into interpreter.inputBuffer
  //ARDUINO SPECIFIC
  while(Serial.available() > 0) {
    //ARDUINO SPECIFIC
    byte x = Serial.read();
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
  update_lights();
  delay(2000);
  light_set_channel(0, 255);
}

void loop() {
  read_serial();
  update_lights();
  // ARDUINO SPECIFIC
  motor.update();
}