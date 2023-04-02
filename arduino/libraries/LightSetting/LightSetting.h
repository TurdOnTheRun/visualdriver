/*
  LightSetting.h - Library for controlling LightSetting.
  Created by Maximilian Weber, April 2, 2023.

  Types:
  1 - Static
  2 - Linear
  3 - Bezier
*/
#ifndef LightSetting_h
#define LightSetting_h

#include "Arduino.h"

class LightSetting {
  private:
    //Possible Settings 
    byte STATICLIGHT = 10
    byte STATICFLASH = 11
    byte LINEARDIMM = 20
    byte BEZIERDIMM = 30


    byte _type;
    byte _state1;
    byte _state2;
    byte _steptime;
    byte _set1;
    byte _set2;
    byte _set3;
    byte _set4;
    byte _set5;

    byte _state;
    unsigned long _passed;
    unsigned long _laststep;

    // General
    int _newstate;
    int _steps;

    // Bezier
    unsigned int _bezierstep;
    float lerp(float n1, float n2, float perc);
    float bezier(byte step);

    float _bz;

    float _i;

    float _xa;
    float _ya;
    float _xb;
    float _yb;
    float _xc;
    float _yc;

    float _xm;
    float _ym;
    float _xn;
    float _yn;

    float _diff;

    float _y;
    
  public:
    LightSetting(byte type, byte state1, byte state2, byte steptime, byte set1, byte set2, byte set3, byte set4, byte set5);
    // init returns first state
    byte init(unsigned long now, byte lightid);
    // get state at current timestamp
    byte get_state(unsigned long now, byte lightid);
    byte get_type();
    void set_state(byte newstate);
    bool rising();
    bool changing();
};

#endif
