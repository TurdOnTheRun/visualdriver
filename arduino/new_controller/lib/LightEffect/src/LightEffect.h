/*
  LightEffect.h - Library for controlling LightEffect.
  Created by Maximilian Weber, April 9, 2023.

  Types:
  100-109 - Vibrato Types
  110-119 - Strobe Types
*/
#ifndef LightEffect_h
#define LightEffect_h

#include "Arduino.h"

//Possible Settings 
static const byte UPVIBRATO = 100;
static const byte DOWNVIBRATO = 101;
static const byte UPDOWNVIBRATO = 102;

static const byte MILLISTROBE = 110;
static const byte DECISTROBE = 111;


class LightEffect {
  private:
    byte _type;
    float _amplitude;
    unsigned int _steptime;
    byte _set1;
    byte _set2;
    byte _set3;
    byte _set4;
    byte _set5;
    byte _set6;

    float _delta = 0.0;
    int _newstate;
    unsigned long _passed;
    unsigned long _laststep = 0;
    byte _usercount = 0;

    // Vibrato variables and functions
    float _vibratostepangle = (float) 2 * M_PI / 50; //50 steps per period
    float _vibratoangle = 0;
    float _upvibrato(float angle);
    float _downvibrato(float angle);
    float _updownvibrato(float angle);

    // Strobe variables
    boolean _on = true;
    void _set_strobe_delta(byte lightid);

    int _steps;
    
  public:
    LightEffect();
    LightEffect(byte type, byte amplitude, byte steptime, byte set1, byte set2, byte set3, byte set4, byte set5, byte set6);
    void init(unsigned long now);
    // get state at current timestamp
    // Always works with _delta. Either multiplied or added
    byte get_state(unsigned long now, byte lightid, byte state);
    byte get_type();
    // user management
    void usercount_up();
    void usercount_down();
    boolean is_unused();
};

#endif