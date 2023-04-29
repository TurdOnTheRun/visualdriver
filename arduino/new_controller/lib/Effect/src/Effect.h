/*
  Effect.h - Library for controlling Effect.
  Created by Maximilian Weber, April 9, 2023.
*/
#ifndef Effect_h
#define Effect_h

#include "Arduino.h"

class Channel;

class Effect {
  private:
    byte _type;
    Channel* _amplitude;
    Channel* _steptime;
    byte _set1;
    byte _set2;
    byte _set3;
    byte _set4;
    byte _set5;
    byte _set6;

    float _delta = 0.0;
    int _newstate;
    unsigned int _newsteptime;
    float _newamplitude;
    unsigned long _passed;
    unsigned long _laststep = 0;
    int _amplitudedirection = 1;
    byte _steptimefactor = 1;
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
    Effect();
    Effect(byte type, Channel* amplitude, Channel* steptime, byte set1, byte set2, byte set3, byte set4, byte set5, byte set6);
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