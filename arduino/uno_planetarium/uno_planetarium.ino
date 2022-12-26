#include <SerialInterpreter.h>
#include <Light.h>
#include <PWM.h>


class UnoLight: public Light {
  private:
    int32_t _frequency = 31000; //frequency (in Hz)
    
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

SerialInterpreter interpreter = SerialInterpreter();

void setup(){
  //SETUP USB SERIAL  
  Serial.begin(115200);
  
  //initialize all timers except for 0, to save time keeping functions
  InitTimersSafe(); 

  motor.init();
  initLights();
  setAll(7,50,3,255,0,0,0,0,0);
}

void loop(){
  readSerial();
  updateLights();
  motor.update();
}

void readSerial() {
  // receive data from Python and save it into inputBuffer
  while(Serial.available() > 0) {
    
    byte x = Serial.read();

    // the order of these IF clauses is significant
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

  if (id == 220) {
    state1 = interpreter.inputBuffer[1];
    steptime = interpreter.inputBuffer[2];
    motor.setto(state1,steptime);
    return;
  } else if (id == 221) {
    motor.changedirection();
    return;
  }

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
  else if(id < 50) {
    //Shutter  
    lightid = id % 10;
    type = 4;
    state1 = interpreter.inputBuffer[1];
    steptime = interpreter.inputBuffer[2];
  }
  else if(id < 60) {
    // Lightning Disappear  
    lightid = id % 10;
    type = 5;
    state1 = interpreter.inputBuffer[1];
    state2 = interpreter.inputBuffer[2];
    // steptime for dimming    
    steptime = interpreter.inputBuffer[3];
    // lightning time in ms   
    set1 = interpreter.inputBuffer[4];
  }
  else if(id < 70) {
    // Lightning Appear  
    lightid = id % 10;
    type = 6;
    state1 = interpreter.inputBuffer[1];
    state2 = interpreter.inputBuffer[2];
    // steptime for dimming
    steptime = interpreter.inputBuffer[3];
    // lightning time in ms
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
  else if(id < 111) {
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


//  Serial.println(id);
//  Serial.println(state1);
//  Serial.println(state2);
//  Serial.println(steptime);
//  Serial.println();
  
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
