#include <SoftwareSerial.h>
SoftwareSerial SwSerial(11, 12); // RX, TX
SoftwareSerial SerialBLE(11, 12); // RX, TX

//Available Pins:
//2,3,5,6,7,8,9,10
int light1 = 2;
int light2 = 3;
int light3 = 5;
int light4 = 6;
int light5 = 7;
int light6 = 8;
int light7 = 9;
int light8 = 10;

int baseBrightness = 200;

void setup() {
  //SETUP BLUETOOTH
  Serial.begin(9600);
  SerialBLE.begin(9600);  
  
  // SET PIN FREQUENCIES TO 31kHz  
  int eraser = 7;       // this is 111 in binary and is used as an eraser
  int prescaler = 1;    // this could be a number in [1 , 6]. 1 corresponds to 31000 Hz (fastest)   
  TCCR2B &= ~eraser;    // this operation (AND plus NOT), set the three bits in TCCR2B to 0
  TCCR3B &= ~eraser;
  TCCR4B &= ~eraser;
  TCCR2B |= prescaler;  //this operation (OR), replaces the last three bits in TCCR2B with our new value 001
  TCCR3B |= prescaler;
  TCCR4B |= prescaler;

  //SET LIGHTS
  pinMode(light1, OUTPUT);
  pinMode(light2, OUTPUT);
  pinMode(light3, OUTPUT);
  pinMode(light4, OUTPUT);
  pinMode(light5, OUTPUT);
  pinMode(light6, OUTPUT);
  pinMode(light7, OUTPUT);
  pinMode(light8, OUTPUT);

  setAll(baseBrightness);
}

void loop() {
  while (SerialBLE.available()) {
    int code = SerialBLE.parseInt();
    //lights can have lightId 1-8 (8 lights total)
    //lightId 9 applies intensity to all lights       
    //1000 <= code <= 9255
    if (code > 999 && code < 9256){
      int lightId = (code / 1000U) % 10;
      int intensity = code - (lightId * 1000);
      if (intensity > -1 && intensity < 256){
        setlight(lightId, intensity);
      }
    }
  }
}

void setAll(int intensity){
  analogWrite(light1, intensity);
  analogWrite(light2, intensity);
  analogWrite(light3, intensity);
  analogWrite(light4, intensity);
  analogWrite(light5, intensity);
  analogWrite(light6, intensity);
  analogWrite(light7, intensity);
  analogWrite(light8, intensity);
}

void setlight(int lightId, int intensity){
  switch(lightId){
    case 1:
      analogWrite(light1, intensity);
      break;
    case 2:
      analogWrite(light2, intensity);
      break;
    case 3:
      analogWrite(light3, intensity);
      break;
    case 4:
      analogWrite(light4, intensity);
      break;
    case 5:
      analogWrite(light5, intensity);
      break;
    case 6:
      analogWrite(light6, intensity);
      break;
    case 7:
      analogWrite(light7, intensity);
      break;
    case 8:
      analogWrite(light8, intensity);
      break;
    case 9:
      setAll(intensity);
      break;
  }
}
