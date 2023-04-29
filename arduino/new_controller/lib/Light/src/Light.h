/*
  Light.h - Library for controlling Light.
  Created by Maximilian Weber, April 2, 2023.
*/
#ifndef Light_h
#define Light_h

#include "Arduino.h"
#include "Channel.h"
#include "Effect.h"


class Light {
  private:
    byte _id;
    byte _pinstate; //state currently set on pin (actual current state)
    Channel* _channel;
    void set_pinstate();
    virtual void pin_write();
    virtual void set_pin_frequency(); //only necessary for uno
  
  protected:
    byte _pin;
    byte _newstate;
    byte _statemap [101] = { 0,2,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,68,70,72,74,77,80,83,86,89,92,95,99,103,107,111,115,120,125,130,135,141,147,153,159,165,172,180,188,196,205,214,224,234,244,255 };

  public:
    Light(byte id, byte pin, Channel* channel);
    void init();
    void update(unsigned long now);
    void set_channel(Channel* channel);
    byte get_id();
};

#endif
