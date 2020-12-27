#include <Light.h>
#include <PWM.h>

//class Light {
//  private:
//    byte id;
//    byte pin;
//    byte state;
//    byte tostate;
//    byte steptime;
//    byte type = 1;
//    unsigned long laststep;
//    int32_t frequency = 50000; //frequency (in Hz)
//    
//  public:
//
//    Light(byte id, byte pin) {
//      this->pin = pin;
//      this->id = id;
//    }
//
//    void init() {
//      pinMode(pin, OUTPUT);
//      //sets the frequency for the specified pin
//      SetPinFrequencySafe(pin, frequency);
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
//      pwmWrite(pin, newstate);
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
//
//};


class UnoLight: public Light {
  private:
    int32_t _frequency = 50000; //frequency (in Hz)
    
  public:
    UnoLight(byte id, byte pin):Light(id, pin){};
    void init() {
      pinMode(_pin, OUTPUT);
      //sets the frequency for the specified pin
      SetPinFrequencySafe(_pin, _frequency);
    };
    void setstate(byte newstate) {
      pwmWrite(_pin, newstate);
      _state = newstate;
      _laststep = millis();
    };
};


// Derived class
class Motor {
  protected:
    const byte RPWM_pin = 5;
    const byte LPWM_pin = 6;
    byte OUT_pin;
    byte NOTOUT_pin;
    const byte MAXIMAL_SPEED_DIFFERENCE = 5;
    const byte MAXIMUM_SPEED = 110;
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


//3, 9, 10
const byte light1 = 3;
const byte light2 = 9;
const byte light3 = 10;

const byte numberoflights = 3;

Motor motor = Motor();

UnoLight lights[numberoflights] = {
  UnoLight(1, light1),
  UnoLight(2, light2),
  UnoLight(3, light3),
};

const byte buffSize = 40;
byte inputBuffer[buffSize];
const char startMarker = '<';
const char endMarker = '>';
byte bytesRecvd = 0;
boolean readInProgress = false;
boolean newData = false;

void setup(){
  //SETUP USB SERIAL  
  Serial.begin(115200);
  
  //initialize all timers except for 0, to save time keeping functions
  InitTimersSafe(); 

  motor.init();
  initLights();
  setAll(0,20,10);
}

void loop(){
  readSerial();
  updateLights();
  motor.update();
}

void readSerial() {
  // receive data from Python and save it into inputBuffer
  while(Serial.available() > 0 && newData == false) {
    
    byte x = Serial.read();

    // the order of these IF clauses is significant
      
    if (x == endMarker) {
      readInProgress = false;
      inputBuffer[bytesRecvd] = 0;
      newData = true;
      parseData();
      newData = false;
    }
    
    if(readInProgress) {
      inputBuffer[bytesRecvd] = x;
      bytesRecvd ++;
      if (bytesRecvd == buffSize) {
        bytesRecvd = buffSize - 1;
      }
    }
    
    if (x == startMarker) {
      bytesRecvd = 0; 
      readInProgress = true;
    }
  }
}

void parseData() {
  // split the data into its parts

  byte id = inputBuffer[0];
  //Serial.println(id);
  byte lightid;
  byte type;
  byte state;
  byte steptime;

  boolean all = false;
  byte alltype;

  if (id == 200) {
    state = inputBuffer[1];
    steptime = inputBuffer[2];
    motor.setto(state,steptime);
    return;
  } else if (id == 210) {
    motor.changedirection();
    return;
  }

  if(id > 99 && id < 110){
    all = true;
    alltype = id % 10;
    id = alltype*10;
  } 
  
  if(id < 10) {
    //Direct    
    lightid = id % 10;
    type = 0;
    state = inputBuffer[1];
    steptime=0;
  } 
  else if(id < 20) {
    //Linear    
    lightid = id % 10;
    type = 1;
    state = inputBuffer[1];
    steptime = inputBuffer[2];
  }
  else if(id < 30) {
    //Strobe  
    lightid = id % 10;
    type = 2;
    state = inputBuffer[1];
    steptime = inputBuffer[2];
  }

  //Serial.println(type);
  //Serial.println(state);
  //Serial.println(steptime);
  
  if(all){
    //Serial.println("all");
    setAll(alltype,state,steptime);
  } else {
    //Serial.println(lightid);
    setLight(lightid,type,state,steptime);
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

void setAll(byte type, byte tostate, byte steptime) {
  for(int i = 0; i < numberoflights; ++i) {
    lights[i].setto(type,tostate,steptime);
  };
}

void setLight(byte id, byte type, byte tostate, byte steptime) {
  lights[id].setto(type,tostate,steptime);
}


























//void executeCommands() {
//  if(newDataAvailable) {
//    //lights can have lightId 1-8 (8 lights total)
//    //lightId 9 applies intensity to all lights       
//    //1000 <= code <= 9255
//    if (code > 999 && code < 9256) {
//      int id = (code / 1000U) % 10;
//      if ((id > 0 && id < 4) || id == 9){
//        int intensity = code - (id * 1000);
//        if (intensity > -1 && intensity < 256){
//          setlight(id, intensity);
//        }
//      }
//      // Id 5 sets the speed of the motor      
//      else if (id == 5){
//        int x = code - (id * 1000);
//        if (x > -1 && x < MAXIMUM_SPEED){
//          setSpeed(x);
//        } else if (x == 555) {
//          setForwards();
//        } else if (x == 666) {
//          setBackwards();
//        } else if (x == 777) {
//          changeDirections();
//        }
//      }
//    }
//    newDataAvailable = false;
//  }
//}
//
//void setAll(int intensity){
//  pwmWrite(light1, intensity);
//  pwmWrite(light2, intensity);
//  pwmWrite(light3, intensity);
//}
//
//void setlight(int lightId, int intensity){
//  switch(lightId){
//    case 1:
//      pwmWrite(light1, intensity);
//      break;
//    case 2:
//      pwmWrite(light2, intensity);
//      break;
//    case 3:
//      pwmWrite(light3, intensity);
//      break;
//    case 9:
//      setAll(intensity);
//      break;
//  }
//}
//
//void setSpeed(int x){
//  if (x > SPEED){
//    if (x - SPEED > MAXIMAL_SPEED_DIFFERENCE){
//      for(int i=SPEED; i<=x; i++){
//        analogWrite(NOTOUT,0);
//        analogWrite(OUT,i);
//        SPEED = i;
//        delay(10);
//      } 
//    } else {
//        analogWrite(NOTOUT,0);
//        analogWrite(OUT,x);
//        SPEED = x;
//      }
//  } else if (x < SPEED){
//      if (SPEED - x > MAXIMAL_SPEED_DIFFERENCE){
//        for(int i=SPEED; i>=x; i--){
//          analogWrite(NOTOUT,0);
//          analogWrite(OUT,i);
//          SPEED = i;
//          delay(10);
//        }
//      } else {
//        analogWrite(NOTOUT,0);
//        analogWrite(OUT,x);
//        SPEED = x;
//      }
//  }
//}
//
//void setForwards(){
//  if (OUT != LPWM_pin){
//    changeDirections();
//  }
//}
//
//void setBackwards(){
//  if (OUT == LPWM_pin){
//    changeDirections();
//  }
//}
//
//void changeDirections(){
//    int tempSpeed = SPEED;
//    int tempOut = OUT;
//    setSpeed(0);
//    OUT = NOTOUT;
//    NOTOUT = tempOut;
//    setSpeed(tempSpeed);
//}
//
//void toStop(){
//  setSpeed(0);
//}
