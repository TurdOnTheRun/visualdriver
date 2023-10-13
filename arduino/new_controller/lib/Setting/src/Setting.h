/*
  Setting.h - Library for controlling Setting.
  Created by Maximilian Weber, April 2, 2023.

  Types:
  1 - 9 - Static Types
  10-19 - Linear Types
  20-29 - Bezier Types
*/
#ifndef Setting_h
#define Setting_h

#include "Arduino.h"
class Channel;

class Setting {
  private:
    byte _type=0;
    Channel* _inputA=nullptr;
    Channel* _inputB=nullptr;

    byte _state=0;
    byte _state1=0;
    byte _state2=0;
    byte _steptime=0;
    byte _setA=0;
    byte _setB=0;
    byte _setC=0;
    byte _setD=0;


    unsigned int _steps=0;
    unsigned long _laststep = 0;

    // General
    int _newstate=0;

    // Bezier
    unsigned int _bezierstep=0;
    unsigned int _beziersteps=0;
    float lerp(float n1, float n2, float perc);
    float bezier(unsigned int step);

    float _bz=0;

    float _i=0;

    float _ya=0;
    float _yb=0;
    float _yc=0;

    float _ym=0;
    float _yn=0;

    float _diff=0;

    float _y=0;
    
  public:
    Setting();
    Setting(byte type, byte set1, byte set2, byte set3, byte set4, byte set5, byte set6);
    // get state at current timestamp
    byte get_state(unsigned long now, byte lightid);
    byte get_type();
    bool rising();
    bool changing();
};

#endif
