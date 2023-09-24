#include<Wire.h>
#define deviceAddress 0b1101000   //0x68

// On Arduino Mega
// Connect 20 to SDA
// Connect 21 to SCL
// Connect 5V to VCC
// Connect GND to GND
// Run Script

void setup() 
{
  Wire.begin();   //TWI Bus is formed  
  Wire.beginTransmission(deviceAddress); //device address and STSRT command are queued
  Wire.write(0x0E); //Control Register Address is queued
  // 0x48 sets SQW to 1.024kHz
  Wire.write(0x48); //Data for Control Register is queued
  Wire.endTransmission(); //queued information are transferred under ACK; STOP
}

void loop() 
{
  
}