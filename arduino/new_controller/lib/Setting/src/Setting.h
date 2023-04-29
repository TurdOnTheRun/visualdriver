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

//Possible Settings 
static const byte STATICLIGHT = 1;
static const byte STATICFLASH = 2;
static const byte STATICMACHINE = 3;
static const byte LINEARDIMM = 10;
static const byte BEZIERDIMM = 20;

class Setting {
  private:
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
    byte _usercount = 0;
    unsigned long _passed;
    unsigned long _laststep = 0;

    // General
    int _newstate;
    int _steps;

    // Bezier
    unsigned int _bezierstep;
    unsigned int _beziersteps;
    float lerp(float n1, float n2, float perc);
    float bezier(unsigned int step);

    float _bz;

    float _i;

    float _ya;
    float _yb;
    float _yc;

    float _ym;
    float _yn;

    float _diff;

    float _y;
    
  public:
    Setting();
    Setting(byte type, byte state1, byte state2, byte steptime, byte set1, byte set2, byte set3, byte set4, byte set5);
    void init(unsigned long now);
    // get state at current timestamp
    byte get_state(unsigned long now, byte lightid);
    byte get_type();
    void set_state(unsigned long now, byte newstate);
    bool rising();
    bool changing();
    // user management
    void usercount_up();
    void usercount_down();
    boolean is_unused();
};

#endif
