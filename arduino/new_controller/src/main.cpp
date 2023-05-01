#include <Light.h>
#include <Effect.h>
#include <Channel.h>
#include <Setting.h>
#include <Controlls.h>
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
const byte light1 = 7;
const byte light2 = 3;
const byte light3 = 2;
const byte light4 = 8; 
// const byte light4 = 5;
// const byte light5 = 6;
// const byte light6 = 9;
// const byte light7 = 10;
// const byte light8 = 11;
// const byte light9 = 12;

// ARDUINO SPECIFIC
const byte numberOfLights = 4;
const byte numberOfSettings = 4;
const byte numberOfEffects = 10;
const byte numberOfChannels = 21;

// ARDUINO SPECIFIC
Setting settings[numberOfSettings] = {
  Setting(SETTING_LINEARDIMM,0,30,40,0,0,0,0,0),
  Setting(),
  Setting(),
  Setting(),
};

Effect effects[numberOfEffects];

// ARDUINO SPECIFIC
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
Light lights[numberOfLights] = {
  Light(0, light1, &channels[3]),
  Light(1, light2, &channels[3]),
  Light(2, light3, &channels[3]),
  Light(3, light4, &channels[3]),
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
      set2 = interpreter.inputBuffer[2];
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
  update_lights();
}

void loop() {
  read_serial();
  update_lights();
}