/*
  Effect.h - Library for controlling Effect.
  Created by Maximilian Weber, April 9, 2023.
*/
#ifndef Effect_h
#define Effect_h

#include "Arduino.h"
#include "Controlls.h"

class Channel;

class Effect {
  private:
    byte _type;
    Channel* _amplitude;
    Channel* _steptime;
    const float* _perlinarray;
    byte _set1;
    byte _set2;
    byte _set3;
    byte _set4;
    byte _set5;
    byte _set6;

    float _delta = 0.0f;
    int _direction = 1;
    int _newstate;
    unsigned int _newsteptime;
    float _newamplitude;
    unsigned long _passed;
    unsigned long _laststep = 0;
    byte _steptimefactor = 1;
    byte _usercount = 0;

    float _position = 0.0f; //position along wave or perlin
    int _get_direction(byte lightid);

    // Vibrato variables and functions
    static constexpr float _vibratostepangle = (float) 2 * M_PI / 50; //50 steps per period
    float _upvibrato(float angle);
    float _downvibrato(float angle);
    float _updownvibrato(float angle);

    // Strobe variables
    boolean _on = true;
    float _strobe(byte lightid);

    // Perlin Noise
    unsigned int _index1;
    unsigned int _index2;
    float _inter; //distance between two indexes (>0; <1)
    // float _perlin_array[PERLIN_SIZE] = {};
    // void _perlin_setup();
    float _perlin_calculate();
    
  public:
    Effect();
    Effect(byte type, Channel* amplitude, Channel* steptime, const float* perlinarray, byte set1, byte set2, byte set3, byte set4, byte set5, byte set6);
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