#include <Light.h>
#include <SerialInterpreter.h>


//Available Pins:
//2,3,5,6,7,8,9,10
const byte light0 = 2;
const byte light1 = 3;
const byte light2 = 7;
const byte light3 = 8;
const byte light4 = 5;
const byte light5 = 6;
const byte light6 = 9;
const byte light7 = 10;
const byte light8 = 11;
const byte light9 = 12;

//const byte numberoflights = 10;
const byte numberoflights = 4;

Light lights[numberoflights] = {
  Light(0, light0),
  Light(1, light1),
  Light(2, light2),
  Light(3, light3),
//  Light(5, light5),
//  Light(6, light6),
//  Light(7, light7),
//  Light(8, light8),
//  Light(9, light9),
//  Light(10, light10),
};

byte baseBrightness = 30;

SerialInterpreter interpreter = SerialInterpreter();

void setup() {
  //SETUP BLUETOOTH
//  Serial.begin(9600);
  Serial1.begin(115200);  
  
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

  initLights();
  setAll(1,baseBrightness,0,40,0,0,0,0,0);
}

void loop() {
  readSerial();
  updateLights();
}

void readSerial() {
  // receive data from Python and save it into interpreter.inputBuffer
  while(Serial1.available() > 0) {
    
    byte x = Serial1.read();
    bool isEnd = interpreter.processByte(x);
    
    if(isEnd){
      parseData();
    }
    
  }
}

void parseData() {
  // split the data into its parts

  byte id = interpreter.inputBuffer[0];
  //Serial.println(id);
  byte lightid;
  byte type;
  byte state1;
  byte state2;
  byte steptime;
  byte set1;
  byte set2;
  byte set3;
  byte set4;
  byte set5;

  boolean all = false;
  byte alltype;

  if(id > 199 && id < 220){
    all = true;
    alltype = id - 200;
    id = alltype*10;
  } 
  
  if(id < 10) {
    //Direct    
    lightid = id % 10;
    type = 0;
    state1 = interpreter.inputBuffer[1];
    steptime = 0;
  } 
  else if(id < 20) {
    //Strobe    
    lightid = id % 10;
    type = 1;
    state1 = interpreter.inputBuffer[1];
    steptime = interpreter.inputBuffer[2];
  }
  else if(id < 30) {
    //Linear  
    lightid = id % 10;
    type = 2;
    state1 = interpreter.inputBuffer[1];
    steptime = interpreter.inputBuffer[2];
  }
  else if(id < 40) {
    //Direct to Linear  
    lightid = id % 10;
    type = 3;
    state1 = interpreter.inputBuffer[1];
    state2 = interpreter.inputBuffer[2];
    steptime = interpreter.inputBuffer[3];
  }
  else if(id < 50) {
    //Lightning  
    lightid = id % 10;
    type = 4;
    state1 = interpreter.inputBuffer[1];
    steptime = interpreter.inputBuffer[2];
  }
  else if(id < 60) {
    //Lightning Disappear  
    lightid = id % 10;
    type = 5;
    state1 = interpreter.inputBuffer[1];
    state2 = interpreter.inputBuffer[2];
    //steptime for dimming    
    steptime = interpreter.inputBuffer[3];
    //lightning time in ms
    set1 = interpreter.inputBuffer[4];
  }
  else if(id < 70) {
    //Lightning Appear   
    lightid = id % 10;
    type = 6;
    state1 = interpreter.inputBuffer[1];
    state2 = interpreter.inputBuffer[2];
    //Steptime for dimming
    steptime = interpreter.inputBuffer[3];
    //Lightning time in ms
    set1 = interpreter.inputBuffer[4];
  }
  else if(id < 80) {
    //Machine Gun  
    lightid = id % 10;
    type = 7;
    state1 = interpreter.inputBuffer[1];
    state2 = interpreter.inputBuffer[2];
    steptime = interpreter.inputBuffer[3];
  }
  else if(id < 90) {
    //Accelerating Strobe  
    lightid = id % 10;
    type = 8;
    state1 = interpreter.inputBuffer[1];
    steptime = interpreter.inputBuffer[2];
    set1 = interpreter.inputBuffer[3];
    set2 = interpreter.inputBuffer[4];
  }
  else if(id < 100) {}
  else if(id < 110) {
    //Bezier Dimm  
    lightid = id % 10;
    type = 10;
    state1 = interpreter.inputBuffer[1];
    state2 = interpreter.inputBuffer[2];
    steptime = interpreter.inputBuffer[3];
    set1 = interpreter.inputBuffer[4];
    set2 = interpreter.inputBuffer[5];
    set3 = interpreter.inputBuffer[6];
    set4 = interpreter.inputBuffer[7];
  }
  else if(id < 120) {
    //Lightning Bezier Appear/Disappear  
    lightid = id % 10;
    type = 11;
    state1 = interpreter.inputBuffer[1];
    state2 = interpreter.inputBuffer[2];
    steptime = interpreter.inputBuffer[3];
    set1 = interpreter.inputBuffer[4];
    set2 = interpreter.inputBuffer[5];
    set3 = interpreter.inputBuffer[6];
    set4 = interpreter.inputBuffer[7];
    //lightning time in ms    
    set5 = interpreter.inputBuffer[8];
  }
  else if(id < 130) {
    //Vibrato  
    lightid = id % 10;
    type = 12;
    state1 = interpreter.inputBuffer[1];
    state2 = interpreter.inputBuffer[2];
    steptime = interpreter.inputBuffer[3];
  }

// Serial.println(type);
// Serial.println(state1);
// Serial.println(state2);
// Serial.println(steptime);
// Serial.println(set1);
// Serial.println(set2);
// Serial.println(set3);
// Serial.println(set4);
// Serial.println(set5);
// Serial.println();
  
  if(all){
    //Serial.println("all");
    setAll(alltype,state1,state2,steptime,set1,set2,set3,set4,set5);
  } else {
    //Serial.println(lightid);
    setLight(lightid,type,state1,state2,steptime,set1,set2,set3,set4,set5);
  }
}

void initLights() {
  for(int i = 0; i < numberoflights; ++i) {
    lights[i].init();
  };
}

void updateLights() {
  for(int i = 0; i < numberoflights; ++i) {
    lights[i].update();
  };
}

void setAll(byte type, byte state1, byte state2, byte steptime, byte set1, byte set2, byte set3, byte set4, byte set5) {
  for(int i = 0; i < numberoflights; ++i) {
    lights[i].setto(type,state1,state2,steptime,set1,set2,set3,set4,set5);
  };
}

void setLight(byte id, byte type, byte state1, byte state2, byte steptime, byte set1, byte set2, byte set3, byte set4, byte set5) {
  lights[id].setto(type,state1,state2,steptime,set1,set2,set3,set4,set5);
}
