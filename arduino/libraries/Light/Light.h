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
    byte _fromstate;
    byte _tostate;
    byte _steptime;
    byte _set1;
    byte _set2;
    byte _set3;
    byte _set4;
    byte _set5;
    unsigned int _bezierstep;
    float lerp(float n1, float n2, float perc);
    float bezier(byte step);

  protected:
    byte _pin;
    byte _state;
    unsigned long _laststep;
    byte _statemap [101] = { 0,2,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,74,76,78,80,82,84,86,88,90,93,96,99,103,107,111,115,120,125,130,136,143,151,160,170,182,196,212,230,255 };
    
  public:
    Light(byte id, byte pin);
    void init();
    void setstate(byte newstate);
    void update();
    void setto(byte type, byte state1, byte state2, byte steptime, byte set1, byte set2, byte set3, byte set4, byte set5);
    bool rising();
    bool changing();
    byte getid();
};

#endif
