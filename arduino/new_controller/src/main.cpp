#include <Light.h>
#include <Motor.h>
#include <Effect.h>
#include <Channel.h>
#include <Setting.h>
#include <Controlls.h>
#include <SerialInterpreter.h>
#include <util/atomic.h>

const bool IS_BOTTOM = false;

// TESTING
// unsigned long communication_testing_now = 0;
// bool communication_testing = false;
// byte communication_testing_channel = 15;
// TESTING END

//RTC Setup
const byte rtcPin = 21;
volatile byte fract = 0;
volatile unsigned long NOW = 0;
unsigned long now = 1;
unsigned long lastNow = 0;

bool syncing = false;
const byte syncPinTop = 13;
const byte syncPinBottom = 18;
unsigned long lastSync = 0;
int syncDelta = 9999;
volatile bool syncNow = false;

// The RTC oscillates at 1024hz. That is 24hz too many.
// Therefore NOW += 1 needs to be suspended at a rate of 24/1024 = 3/128.
// 24/1000 is incorrect because the RTC does not oscillate at 1000hz.
void rtc_millis_routine() {
  fract += 3;
  if(fract >= 128){
    fract -= 128;
  } else {
    NOW += 1;
  }
}

void rtc_setup(){
  attachInterrupt(digitalPinToInterrupt(rtcPin), rtc_millis_routine, FALLING);
}

void rtc_sync_top() {
  if(now >= SYNC_MILLIS){
    digitalWrite(syncPinTop, !digitalRead(syncPinTop));
    if(digitalRead(syncPinTop) == LOW){
      ATOMIC_BLOCK(ATOMIC_RESTORESTATE){
        NOW = 0;
        fract = 0;
      }
    }
  }
}

void rtc_sync_setup_top(){
  pinMode(syncPinTop, OUTPUT);
  digitalWrite(syncPinTop, HIGH);
  ATOMIC_BLOCK(ATOMIC_RESTORESTATE){
    NOW = 0;
    fract = 0;
  }
}

void rtc_sync_teardown_top(){
  pinMode(syncPinTop, INPUT);
}

void rtc_sync_routine_bottom(){
  ATOMIC_BLOCK(ATOMIC_RESTORESTATE){
    NOW = 0;
    fract = 0;
  }
};

void rtc_sync_setup_bottom(){
  pinMode(syncPinBottom, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(syncPinBottom), rtc_sync_routine_bottom, FALLING);
}

void rtc_sync_teardown_bottom(){
  detachInterrupt(digitalPinToInterrupt(syncPinBottom));
  pinMode(syncPinBottom, INPUT);
}

void pwm_setup(){
  //SET PIN FREQUENCIES TO 31kHz  
  int eraser = 7;       // this is 111 in binary and is used as an eraser
  int prescaler = 1;    // this could be a number in [1 , 6]. 1 corresponds to 31000 Hz (fastest)
  // this operation (AND plus NOT), set the three bits in TCCR2B to 0   
  TCCR2B &= ~eraser;    
  TCCR3B &= ~eraser;
  TCCR4B &= ~eraser;
  if(!IS_BOTTOM){ //deactivated 31Hz for pins 11 and 12 for motor
    TCCR1B &= ~eraser; 
  }
  //this operation (OR), replaces the last three bits in TCCR2B with our new value 001
  TCCR2B |= prescaler;  
  TCCR3B |= prescaler;
  TCCR4B |= prescaler;
  if(!IS_BOTTOM){ //deactivated 31Hz for pins 11 and 12 for motor
    TCCR1B |= prescaler;
  }
}

Motor motor = Motor(11, 12);
const byte numberOfLights = 4;

//Available Pins:
//2,3,5,6,7,8,9,10,11,12
const byte light1 = 2;
const byte light2 = 3;
const byte light3 = 5;
const byte light4 = 6; 
const byte light5 = 7;
const byte light6 = 8;
const byte light7 = 9;
const byte light8 = 10;
const byte light9 = 11;
const byte light10 = 12;

const byte numberOfSettings = 10;
const byte numberOfEffects = 10;
const byte numberOfChannels = 21;

Setting settings[numberOfSettings] = {
  Setting(),
  Setting(),
  Setting(),
  Setting(),
  Setting(),
  Setting(),
  Setting(),
  Setting(),
  Setting(),
  Setting(),
};

Effect effects[numberOfEffects];

Channel channels[numberOfChannels] = {
  Channel(0),
  Channel(5),
  Channel(17),
  Channel(34),
  Channel(51),
  Channel(67),
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
  Channel(),
  Channel(),
  Channel(),
  Channel(),
};

Light lights[numberOfLights];

SerialInterpreter interpreter = SerialInterpreter();

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
  }
}

void channel_set_channel(byte channelindex, byte inputchannelindex){
  if(channelindex < numberOfChannels && inputchannelindex < numberOfChannels){
    channels[channelindex].set_channel(&channels[inputchannelindex]);
  }
}

void channel_set_static(byte channelindex, byte state){
  if(channelindex < numberOfChannels){
    channels[channelindex].set_static(state);
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
  for(byte i = 7; i < numberOfChannels; i++) {
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

void now_increase(byte num){
  now += (int) num;
}

void now_decrease(byte num){
  now -= (int) num;
}

void sync_on(){
  if(IS_BOTTOM){
    rtc_sync_setup_bottom();
  } 
  else {
    rtc_sync_setup_top();
  }
  syncing = true;
}

void sync_off(){
  if(IS_BOTTOM){
    rtc_sync_teardown_bottom();
  } 
  else {
    rtc_sync_teardown_top();
  }
  syncing = false;
}

void parse_data() {
  // split the data into its parts

  // TESTING
  // channel_set_static(communication_testing_channel, 30);
  // communication_testing = true;
  // communication_testing_now = now;
  // TESTING END

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

  type = interpreter.inputBuffer[0];
  target = interpreter.inputBuffer[1];

  switch(type){
    case SETTING_STATIC: {
      //set1: state 
      set1 = interpreter.inputBuffer[2];
    } break;

    case SETTING_SINGULARFLASH: {
      //set1: start state
      //set2: to state
      //set3: flash time
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
    } break;

    case SETTING_SINGULARBURST: {
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

    case SETTING_SINGULARLINEAR: {
      //set1: start state
      //set2: to state
      //set3: steptime
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
    } break;

    case SETTING_SINGULARBEZIER: {
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

    case SETTING_SINGULARBEZIERBEFOREFLASH: {
      //set1: start state
      //set2: to state
      //set3: steptime
      //set4: decisteps
      //set5: y1 of bezier input
      //set6: y2 of bezier input
      //set7: flashtime
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
      set4 = interpreter.inputBuffer[5];
      set5 = interpreter.inputBuffer[6];
      set6 = interpreter.inputBuffer[7];
      set7 = interpreter.inputBuffer[8];
    } break;

    case SETTING_SINGULARBEZIERAFTERFLASH: {
      //set1: start state
      //set2: to state
      //set3: steptime
      //set4: decisteps
      //set5: y1 of bezier input
      //set6: y2 of bezier input
      //set7: flashtime
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
      set4 = interpreter.inputBuffer[5];
      set5 = interpreter.inputBuffer[6];
      set6 = interpreter.inputBuffer[7];
      set7 = interpreter.inputBuffer[8];
    } break;

    case SETTING_SINGULARIMPULSETOBEZIERFADEOUT: {
      //set1: attack state
      //set2: attack steptime (for 100 steps)
      //set3: sustain state
      //set4: sustain steptime (for 100 steps)
      //set5: release bezier steptime
      //set6: release bezier decisteps
      //set7: release y1 bezier input
      //set8: release y2 bezier input
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
      set4 = interpreter.inputBuffer[5];
      set5 = interpreter.inputBuffer[6];
      set6 = interpreter.inputBuffer[7];
      set7 = interpreter.inputBuffer[8];
      set8 = interpreter.inputBuffer[9];
    } break;

    case SETTING_SINWAVE: {
      //set1: from state channel
      //set2: to state channel
      //set3: steptime channel
      //set4: decisteps for intervalsteps channel
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
      set4 = interpreter.inputBuffer[5];
    } break;

    case SETTING_LINEARWAVE: {
      //set1: from state channel
      //set2: to state channel
      //set3: steptime channel
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
    } break;

    case SETTING_LINEARSAW: {
      //set1: from state channel
      //set2: to state channel
      //set3: steptime channel
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
    } break;

    case SETTING_BEZIERWAVE: {
      //set1: from state channel
      //set2: to state channel
      //set3: steptime channel
      //set4: decisteps for intervalsteps channel
      //set5: y1 channel
      //set6: y2 channel
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
      set4 = interpreter.inputBuffer[5];
      set5 = interpreter.inputBuffer[6];
      set6 = interpreter.inputBuffer[7];
    } break;

    case SETTING_BEZIERSAW: {
      //set1: from state channel
      //set2: to state channel
      //set3: steptime channel
      //set4: decisteps for intervalsteps channel
      //set5: y1 channel
      //set6: y2 channel
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
      set4 = interpreter.inputBuffer[5];
      set5 = interpreter.inputBuffer[6];
      set6 = interpreter.inputBuffer[7];
    } break;

    case SETTING_SQUAREWAVE: {
      //set1: from state channel
      //set2: to state channel
      //set3: from steptime channel
      //set4: to steptime channel
      //set5: from steptime-factor channel
      //set6: to steptime-factor channel
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
      set4 = interpreter.inputBuffer[5];
      set5 = interpreter.inputBuffer[6];
      set6 = interpreter.inputBuffer[7];
    } break;

    case SETTING_NOISE: {
      //set1: from state channel
      //set2: to state channel
      //set3: steptime channel
      //set4: steptime-factor channel
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
      set4 = interpreter.inputBuffer[5];
    } break;

    case SETTING_SEEDNOISE: {
      //set1: from state channel
      //set2: to state channel
      //set3: steptime channel
      //set4: steptime-factor channel
      //set5: seed channel
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
      set4 = interpreter.inputBuffer[5];
      set5 = interpreter.inputBuffer[6];
    } break;

    case SETTING_PERLINNOISE: {
      //set1: from state channel
      //set2: to state channel
      //set3: steptime channel
      //set4: steptime-factor channel
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
      set4 = interpreter.inputBuffer[5];
    } break;

    case EFFECT_NONE: {
      // Does not need any input
    } break;

    case EFFECT_INVERSE: {
      // Does not need any input
    } break;

    case EFFECT_LASTORZERO: {
      // Does not need any input
    } break;

    case EFFECT_ADD: {
      //set1: y in state = state + y
      set1 = interpreter.inputBuffer[2];
    } break;

    case EFFECT_SUBTRACT: {
      //set1: y in state = state - y
      set1 = interpreter.inputBuffer[2];
    } break;

    case EFFECT_ADDPERCENTAGE: {
      //set1: y in state = state + (state * y/100)
      set1 = interpreter.inputBuffer[2];
    } break;

    case EFFECT_SUBTRACTPERCENTAGE: {
      //set1: y in state = state - (state * y/100)
      set1 = interpreter.inputBuffer[2];
    } break;

    case EFFECT_SEQUENCEDLIGHTSTROBE: {
      //set1: steptime channel
      //set2: darkstep channel
      //set3: byte 1 of sequence unsigned long
      //set4: byte 2 of sequence unsinged long
      //set5: byte 3 of sequence unsinged long
      //set6: byte 4 of sequence unsinged long
      set1 = interpreter.inputBuffer[2];
      set2 = interpreter.inputBuffer[3];
      set3 = interpreter.inputBuffer[4];
      set4 = interpreter.inputBuffer[5];
      set5 = interpreter.inputBuffer[6];
      set6 = interpreter.inputBuffer[7];
    } break;

    case EFFECT_PERCENTAGE: {
      //set1:  y in state = state * y/100
      set1 = interpreter.inputBuffer[2];
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

    case CHANNEL_SET_STATIC: {
      //set1: staticState
      set1 = interpreter.inputBuffer[2];
      channel_set_static(target, set1);
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

    case NOW_INCREASE: {
      //target: byte by which the delta should be increased
      now_increase(target);
      return;
    } break;

    case NOW_DECREASE: {
      //target: byte by which the delta should be decreased
      now_decrease(target);
      return;
    } break;

    case SYNC_ON: {
      sync_on();
      return;
    } break;

    case SYNC_OFF: {
      sync_off();
      return;
    } break;

    case MOTOR_SPEED: {
      // target: state
      // set1: steptime
      set1 = interpreter.inputBuffer[2];
      motor.set_to(target, set1, now);
      return;
    } break;

    case MOTOR_DIRECTION: {
      motor.change_direction(now);
      return;
    } break;

    default: {
      return;
    } break;
  }

  // Settings
  if(type < SETTING_SINGULAR_DIVIDER){
    setting_add(target, Setting(type, set1, set2, set3, set4, set5, set6, set7, set8));
  }
  else if(type < SETTING_EFFECT_DIVIDER){
    setting_add(target, Setting(type, &channels[set1], &channels[set2], &channels[set3], &channels[set4], &channels[set5], &channels[set6]));
  } 
  else if(type < EFFECT_STEPTIME_DIVIDER){
    effect_add(target, Effect(type, &channels[set1]));
  }
  else if(type < 150){
    effect_add(target, Effect(type, &channels[set1], &channels[set2], set3, set4, set5, set6));
  }
}

void update_lights() {
  for(byte i = 0; i < numberOfLights; i++) {
    lights[i].update(now);
  };
}

void read_serial() {
  // receive data from Python and save it into interpreter.inputBuffer
  if(IS_BOTTOM){
    while(Serial.available() > 0) {   
      byte x = Serial.read();
      bool isEnd = interpreter.processByte(x);
      if(isEnd){
        parse_data();
      }
    }
  } 
  else {
    while(Serial1.available() > 0) {   
      byte x = Serial1.read();
      // Serial.print(x, DEC);
      // Serial.println();
      bool isEnd = interpreter.processByte(x);
      if(isEnd){
        parse_data();
      }
    }
  }

}

void lights_setup() {
  if(IS_BOTTOM){
    lights[0] = Light(1, light1, &channels[0]);
    lights[1] = Light(2, light2, &channels[0]);
    lights[2] = Light(3, light3, &channels[0]);
    lights[3] = Light(4, light4, &channels[0]);
  } else {
    lights[0] = Light(5, light1, &channels[2]);
    lights[1] = Light(6, light2, &channels[2]);
    lights[2] = Light(7, light3, &channels[2]);
    lights[3] = Light(8, light4, &channels[2]);
  }

  for(byte i = 0; i < numberOfLights; i++) {
    lights[i].init();
  };
}

void setup() {
  rtc_setup();
  pwm_setup();
  delay(1000);
  lights_setup();
  update_lights();
  if(IS_BOTTOM){
    Serial.begin(115200);
    motor.init();
  }
  else{
    // Serial.begin(9600);
    delay(2000);
    Serial1.begin(115200);
    delay(1000);
    // clear Serial
    while (Serial1.available() > 0) {
      Serial1.read();
    }
  }
}

void loop() {
  ATOMIC_BLOCK(ATOMIC_RESTORESTATE){
    now = NOW;
  }

  read_serial();
  
  if(syncing){
    if(!IS_BOTTOM){
      rtc_sync_top();
    }
  } 
  else if(now != lastNow){
    lastNow = now;
    update_lights();
    if(IS_BOTTOM){
      motor.update(now);
    }
    // TESTING
    // if(communication_testing && (now - communication_testing_now) > 8){
    //   channel_set_static(communication_testing_channel, 0);
    //   communication_testing = false;
    // }
    // TESTING END
  }
}
