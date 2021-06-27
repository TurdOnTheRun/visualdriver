/*
  Light.h - Library for controlling Light.
  Created by Maximilian Weber, December 23, 2020.
*/
#ifndef Light_h
#define Light_h

#include "Arduino.h"

class Light {
  private:
    byte _id;
    byte _type = 1;
    byte _tostate;
    byte _steptime;
    byte _set1;
    byte _set2;
    byte _set3;

  protected:
    byte _pin;
    byte _state;
    unsigned long _laststep;
    
  public:
    Light(byte id, byte pin);
    void init();
    void setstate(byte newstate);
    void update();
    void setto(byte type, byte state1, byte state2, byte steptime, byte set1, byte set2, byte set3);
    bool rising();
    bool changing();
    byte getid();
};

#endif
