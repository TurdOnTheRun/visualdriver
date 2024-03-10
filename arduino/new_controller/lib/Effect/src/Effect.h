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
    byte _type=0;
    Channel* _channelA=nullptr;
    Channel* _channelB=nullptr;
    byte _varA=0;
    byte _steptime=0;

    int _newstate=0;
    unsigned long _laststep = 0;
    unsigned int _fract = 0;
    byte _steps = 0;
    byte _darksteptracker = 0;

    byte _sequence[SEQUENCE_SIZE] = {0,0,0,0,0,0,0,0,0};
    unsigned int _index = 0;

    byte _get_steptime_adjustment();
    byte _get_state_from_newstate();

  public:
    Effect();
    Effect(byte type, Channel* channel1);
    Effect(byte type, Channel* channel1, Channel* channel2, byte set1, byte set2, byte set3, byte set4);
    // get state at current timestamp
    byte get_state(unsigned long now, byte state, byte lightid);
    byte get_type();
};

#endif