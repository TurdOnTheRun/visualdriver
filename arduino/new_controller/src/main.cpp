#include <Light.h>
#include <LightSetting.h>
#include <LightEffect.h>
#include <SerialInterpreter.h>


// ARDUINO SPECIFIC
void pwm_setup(){
  //SET PIN FREQUENCIES TO 31kHz  
  int eraser = 7;       // this is 111 in binary and is used as an eraser
  int prescaler = 1;    // this could be a number in [1 , 6]. 1 corresponds to 31000 Hz (fastest)   
  TCCR1B &= ~eraser;    // this operation (AND plus NOT), set the three bits in TCCR2B to 0
  TCCR2B &= ~eraser;    
  TCCR3B &= ~eraser;
  TCCR4B &= ~eraser;
  TCCR1B |= prescaler; //this operation (OR), replaces the last three bits in TCCR2B with our new value 001
  TCCR2B |= prescaler;  
  TCCR3B |= prescaler;
  TCCR4B |= prescaler;
}

// ARDUINO SPECIFIC
//Available Pins:
//2,3,5,6,7,8,9,10
const byte light0 = 2;
const byte light1 = 3;
const byte light2 = 7;
const byte light3 = 8;
// const byte light4 = 5;
// const byte light5 = 6;
// const byte light6 = 9;
// const byte light7 = 10;
// const byte light8 = 11;
// const byte light9 = 12;

// ARDUINO SPECIFIC
const byte numberOfLights = 4;
const byte numberOfSettings = 5;
const byte numberOfEffects = (numberOfLights * EFFECTSPERLIGHT) + 1;

// ARDUINO SPECIFIC
// Always must be one more than numberOfLights
LightSetting lightSettings[numberOfSettings] = {
  LightSetting(LINEARDIMM,0,30,40,0,0,0,0,0),
  LightSetting(),
  LightSetting(),
  LightSetting(),
  LightSetting(),
};

LightEffect lightEffects[numberOfEffects];

// ARDUINO SPECIFIC
Light lights[numberOfLights] = {
  Light(0, light0, &lightSettings[0]),
  Light(1, light1, &lightSettings[0]),
  Light(2, light2, &lightSettings[0]),
  Light(3, light3, &lightSettings[0]),
//  Light(5, light5),
//  Light(6, light6),
//  Light(7, light7),
//  Light(8, light8),
//  Light(9, light9),
//  Light(10, light10),
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


void remove_effect(byte lightid, byte effectindex){
  lights[lightid].remove_effect(effectindex);
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
      //set3: steptime multiplier
      //set4: multisetting
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
      set4 = interpreter.inputBuffer[5];
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
  // Serial.begin(9600);
  Serial1.begin(115200);

  pwm_setup();
  lights_setup();
  now = millis();
  settings_setup();
  update_lights();
  add_effect(255, LightEffect(111, 100, 20, 10, 0,0,0,0,0));
}

void loop() {
  read_serial();
  update_lights();
}