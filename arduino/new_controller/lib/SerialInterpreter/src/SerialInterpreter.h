/*
  SerialInterpreter.h - Library for interpreting Serial messages.
  Created by Maximilian Weber, December 26, 2020.
*/
#ifndef SerialInterpreter_h
#define SerialInterpreter_h

#include "Arduino.h"

class SerialInterpreter {
  private:
    const byte buffSize = 40;
    const byte startMarker = 251;
    const byte endMarker = 252;
    byte bytesRecvd = 0;
    
  public:
    bool readInProgress = false;
    byte* inputBuffer;
    SerialInterpreter();
    bool processByte(byte x);
};

#endif
