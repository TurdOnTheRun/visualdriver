#include <PWM.h>

//3, 9, 10
int light1 = 3;
int light2 = 9;
int light3 = 10;

int RPWM_Output = 5;
int LPWM_Output = 6;
int SPEED = 0;
int OUT = -1;
int NOTOUT = -1;
int MAXIMAL_SPEED_DIFFERENCE = 5;

int baseBrightness = 20;
int32_t frequency = 50000; //frequency (in Hz)

void setup(){
  //SETUP USB SERIAL  
  Serial.begin(9600);

  //SET LIGHTS
  pinMode(light1, OUTPUT);
  pinMode(light2, OUTPUT);
  pinMode(light3, OUTPUT);

  //SET MOTOR
  pinMode(RPWM_Output, OUTPUT);
  pinMode(LPWM_Output, OUTPUT);  
  OUT = LPWM_Output;
  NOTOUT = RPWM_Output;
  
  //initialize all timers except for 0, to save time keeping functions
  InitTimersSafe(); 

  //sets the frequency for the specified pins
  SetPinFrequencySafe(light1, frequency);
  SetPinFrequencySafe(light2, frequency);
  SetPinFrequencySafe(light3, frequency);

  setAll(baseBrightness);
}

void loop(){
  while (Serial.available()) {
    int code = Serial.parseInt();
    //lights can have lightId 1-3 (3 lights total)
    //lightId 9 applies intensity to all lights       
    //1000 <= code <= 9255
    if (code > 999 && code < 9256){
      int id = (code / 1000U) % 10;
      if ((id > 0 && id < 4) || id == 9){
        int intensity = code - (id * 1000);
        if (intensity > -1 && intensity < 256){
          setlight(id, intensity);
        }
      }
      // Id 5 sets the speed of the motor      
      else if (id == 5){
        int x = code - (id * 1000);
        if (x > -1 && x < 256){
          setSpeed(x);
        } else if (x == 555) {
          setForwards();
        } else if (x == 666) {
          setBackwards();
        } else if (x == 777) {
          changeDirections();
        }
      }
    }
  }
}

void setAll(int intensity){
  pwmWrite(light1, intensity);
  pwmWrite(light2, intensity);
  pwmWrite(light3, intensity);
}

void setlight(int lightId, int intensity){
  switch(lightId){
    case 1:
      pwmWrite(light1, intensity);
      break;
    case 2:
      pwmWrite(light2, intensity);
      break;
    case 3:
      pwmWrite(light3, intensity);
      break;
    case 9:
      setAll(intensity);
      break;
  }
}

void setSpeed(int x){
  if (x > SPEED){
    if (x - SPEED > MAXIMAL_SPEED_DIFFERENCE){
      for(int i=SPEED; i<=x; i++){
        analogWrite(NOTOUT,0);
        analogWrite(OUT,i);
        SPEED = i;
        delay(5);
      } 
    } else {
        analogWrite(NOTOUT,0);
        analogWrite(OUT,x);
        SPEED = x;
      }
  } else if (x < SPEED){
      if (SPEED - x > MAXIMAL_SPEED_DIFFERENCE){
        for(int i=SPEED; i>=x; i--){
          analogWrite(NOTOUT,0);
          analogWrite(OUT,i);
          SPEED = i;
          delay(5);
        }
      } else {
        analogWrite(NOTOUT,0);
        analogWrite(OUT,x);
        SPEED = x;
      }
  }
}

void setForwards(){
  if (OUT != LPWM_Output){
    changeDirections();
  }
}

void setBackwards(){
  if (OUT == LPWM_Output){
    changeDirections();
  }
}

void changeDirections(){
    int tempSpeed = SPEED;
    int tempOut = OUT;
    setSpeed(0);
    OUT = NOTOUT;
    NOTOUT = tempOut;
    setSpeed(tempSpeed);
}

void toStop(){
  setSpeed(0);
}
