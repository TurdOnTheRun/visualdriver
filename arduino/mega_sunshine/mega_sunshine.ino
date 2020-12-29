#include <Light.h>
#include <SerialInterpreter.h>

//
//class Light {
//  private:
//    byte id;
//    byte pin;
//    byte state;
//    byte tostate;
//    byte steptime;
//    byte type = 1;
//    unsigned long laststep;
//    
//  public:
//
//    Light(byte id, byte pin){
//      this->pin = pin;
//      this->id = id;
//    }
//
//    void init() {
//      pinMode(pin, OUTPUT);
//    }
//
//    void update() {
//      
//      if (changing()){
//        
//        unsigned long passed = millis() - laststep;
//        if (passed < steptime){
//          return;
//        }
//      
//        if(type != 2){
//          //  Linear, etc.
//          int steps = (int) round(passed/steptime);
//  
//          int newstate;
//          
//          if (rising()){
//            
//            newstate = ((int)state)+steps;
//            
//            if (newstate >= tostate || newstate > 255){
//              setstate(tostate);
//            } else {
//              setstate(lowByte(newstate));
//            }
//            
//          } else {
//            
//            newstate = ((int)state)-steps;
//            
//            if (newstate <= tostate || newstate < 0){
//              setstate(tostate);
//            } else {
//              setstate(lowByte(newstate));
//            }
//            
//          }
//        } 
//        else {
//          //  Strobe
//          if(state == 0){
//            setstate(tostate);
//            tostate = 0;
//          } else {
//            tostate = state;
//            setstate(0);
//          }
//        }
//      }
//    }
//
//    void setstate(byte newstate) {
//      analogWrite(pin, newstate);
//      state = newstate;
//      laststep = millis();
//    }
//
//    void setto(byte type_in, byte tostate_in, byte steptime_in) {
//      if(type_in == 0){
//        setstate(tostate_in);
//        tostate = tostate_in;
//      }
//      else if(type_in == 1){
//        if(steptime_in == 0){
//          setstate(tostate_in);
//          tostate = tostate_in;
//        } else {
//          steptime = steptime_in;
//          tostate = tostate_in;
//          laststep = millis();
//        }
//      }
//      else if(type_in == 2){
//        if(state == tostate_in){
//          setstate(0);
//          tostate = tostate_in;
//        } else {
//          setstate(tostate_in);
//          tostate = 0;
//        }
//        steptime = steptime_in;
//      }
//      
//      type = type_in;
//    }
//
//    bool rising() {
//      return (state < tostate);
//    }
//
//    bool changing() {
//      return !(state == tostate);
//    }
//
//    byte getid() {
//      return id;
//    };
//};

//Available Pins:
//2,3,5,6,7,8,9,10
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

const byte numberoflights = 10;

Light lights[numberoflights] = {
  Light(1, light1),
  Light(2, light2),
  Light(3, light3),
  Light(4, light4),
  Light(5, light5),
  Light(6, light6),
  Light(7, light7),
  Light(8, light8),
  Light(9, light9),
  Light(10, light10),
};

byte baseBrightness = 200;

//const byte buffSize = 40;
//byte interpreter.inputBuffer[buffSize];
//const char startMarker = '<';
//const char endMarker = '>';
//byte bytesRecvd = 0;
//boolean readInProgress = false;

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
  setAll(1,200,0,40);
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
    //Linear    
    lightid = id % 10;
    type = 1;
    state1 = interpreter.inputBuffer[1];
    steptime = interpreter.inputBuffer[2];
  }
  else if(id < 30) {
    //Strobe  
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

//  Serial.println(id);
//  Serial.println(state);
//  Serial.println(steptime);
//  Serial.println();
  
  if(all){
    //Serial.println("all");
    setAll(alltype,state1,state2,steptime);
  } else {
    //Serial.println(lightid);
    setLight(lightid,type,state1,state2,steptime);
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

void setAll(byte type, byte state1, byte state2, byte steptime) {
  for(int i = 0; i < numberoflights; ++i) {
    lights[i].setto(type,state1,state2,steptime);
  };
}

void setLight(byte id, byte type, byte state1, byte state2, byte steptime) {
  lights[id].setto(type,state1,state2,steptime);
}
