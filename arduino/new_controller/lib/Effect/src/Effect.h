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
    byte _type=0;
    Channel* _channelA=nullptr;
    byte _varA=0;

    int _newstate=0;

    byte _get_state_from_newstate();

  public:
    Effect();
    Effect(byte type, Channel* channel1);
    // get state at current timestamp
    byte get_state(unsigned long now, byte state);
    byte get_type();
};

#endif