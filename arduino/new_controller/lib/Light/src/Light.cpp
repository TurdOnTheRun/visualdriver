/*
  Light.cpp - Library for controlling Light.
  Created by Maximilian Weber, Dezember 25, 2020.
*/

#include "Arduino.h"
#include "Light.h"
#include "Channel.h"
#include <math.h>

Light::Light(){}

Light::Light(byte id, byte pin, Channel* channel)
{
  _id = id;
  _pin = pin;
  _channel = channel;
}

void Light::init()
{
  pinMode(_pin, OUTPUT);
}

void Light::set_pinstate()
{
  if(_newstate > 100){
    _newstate = 100;
  }
  if(_pinstate != _newstate){
    pin_write();
    _pinstate = _newstate;
  }
}

void Light::pin_write()
{
  analogWrite(_pin, _statemap[_newstate]);
}

void Light::update(unsigned long now)
{
  _newstate = _channel->get_state(now, _id);
  set_pinstate();
}

void Light::set_channel(Channel* channel)
{
  _channel = channel;
}

byte Light::get_id()
{
  return _id;
}
