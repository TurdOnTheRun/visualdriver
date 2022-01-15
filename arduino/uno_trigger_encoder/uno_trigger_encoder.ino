#include<SoftwareSerial.h>
#include <SerialInterpreter.h>
#include <Servo.h>

int encoderA = 3; //Blue
int encoderB = 2; //Purple

// Servo pin = 6
const byte servoPin = 6;
Servo servo;
SerialInterpreter interpreter = SerialInterpreter();

void setup() {
  Serial.begin(115200);
  pinMode(encoderA, INPUT_PULLUP);
  pinMode(encoderB, INPUT_PULLUP);
  delay(1000);
  attachInterrupt(0, aChange, CHANGE);
  attachInterrupt(1, bChange, CHANGE);
}

void loop(){
  readSerial();
}

void readSerial() {
  // receive data from Python and save it into interpreter.inputBuffer
  while(Serial.available() > 0) {
    
    byte x = Serial.read();
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

  
  if(id == 0){
    // Detach servo
    servo.detach();   
  }
  else if(id == 1){
    // Set angle
    byte angle = interpreter.inputBuffer[1];
    if(angle > 180){
      angle = 180;
    }
    servo.attach(servoPin);  // Connect D6 of Arduino with PWM signal pin of servo motor
    servo.write(angle);
  }
}

//Encoder sends 1 for forward motion and -1 for reverse
void sendit(char c){
    Serial.write(c);
}

void aChange(){
  if( digitalRead(encoderB) == 0 ) {
    if ( digitalRead(encoderA) == 0 ) {
      // A fell, B is low
      sendit(-1); // moving reverse
    } else {
      // A rose, B is low
      sendit(1); // moving forward
    }
  }else {
    if ( digitalRead(encoderA) == 0 ) {
      // B fell, A is high
      sendit(1); // moving forward
    } else {
      // B rose, A is high
      sendit(-1); // moving reverse
    }
  }
}

void bChange(){
  if ( digitalRead(encoderA) == 0 ) {
    if ( digitalRead(encoderB) == 0 ) {
      // B fell, A is low
      sendit(1); // moving forward
    } else {
      // B rose, A is low
      sendit(-1); // moving reverse
    }
 } else {
    if ( digitalRead(encoderB) == 0 ) {
      // B fell, A is high
      sendit(-1); // moving reverse
    } else {
      // B rose, A is high
      sendit(1); // moving forward
    }
  }
}
