/*
  SerialInterpreter.h - Library for interpreting Serial messages.
  Created by Maximilian Weber, Dezember 26, 2020.
*/

#include "Arduino.h"
#include "SerialInterpreter.h"

SerialInterpreter::SerialInterpreter()
{
  inputBuffer = new byte[buffSize];
}

bool SerialInterpreter::processByte(byte x)
{
  if (x == endMarker) {
    readInProgress = false;
    inputBuffer[bytesRecvd] = '\0';
    return true;
  }

  if(readInProgress) {
    inputBuffer[bytesRecvd] = x;
    bytesRecvd++;
    if (bytesRecvd == buffSize) {
      bytesRecvd = buffSize - 1;
    }
    return false;
  }

  if (x == startMarker) {
    bytesRecvd = 0; 
    readInProgress = true;
    return false;
  }
}
