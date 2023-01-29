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
    // Bezier
    unsigned int _bezierstep;
    float lerp(float n1, float n2, float perc);
    float bezier(byte step);
    // Vibrato
    bool _hasvibrato = false;
    byte _vibratotype;
    byte _vibratosteptime;
    float _vibratostepangle = (float) 2 * M_PI / 50; //50 steps per period
    float _vibratoangle = 0;
    float _vibratoamplitude; //percentage of state
    float _upvibrato(float angle);
    float _downvibrato(float angle);
    float _updownvibrato(float angle);

  protected:
    byte _pin;
    byte _state; //state without vibrato or other effects
    byte _pinstate; //state currently set on pin (actual current state)
    unsigned long _now;
    unsigned long _passed;
    unsigned long _laststep;
    unsigned long _vibratolaststep;
    byte _statemap [101] = { 0,2,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,68,70,72,74,77,80,83,86,89,92,95,99,103,107,111,115,120,125,130,135,141,147,153,159,165,172,180,188,196,205,214,224,234,244,255 };
    
  public:
    Light(byte id, byte pin);
    void init();
    void setstate(byte newstate);
    void setpinstate(byte newstate);
    void update();
    void setto(byte type, byte state1, byte state2, byte steptime, byte set1, byte set2, byte set3, byte set4, byte set5);
    bool rising();
    bool changing();
    byte getid();
};

#endif
