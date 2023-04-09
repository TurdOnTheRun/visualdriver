/*
  Light.cpp - Library for controlling Light.
  Created by Maximilian Weber, Dezember 25, 2020.
*/

// #include "Arduino.h"
#include "Light.h"
#include <math.h>

Light::Light(byte id, byte pin, LightSetting* setting)
{
  _id = id;
  _pin = pin;
  _setting = setting;
  _setting->usercount_up();
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
    analogWrite(_pin, _statemap[_newstate]);
    _pinstate = _newstate;
  }
}

void Light::set_setting(LightSetting* setting)
{
  _setting->usercount_down();
  _setting = setting;
  _setting->usercount_up();
}

void Light::update(unsigned long now)
{
  _newstate = _setting->get_state(now, _id);
  // for effect in effects:
  //    state = effect.get_state(state, _id)
  set_pinstate();
}

byte Light::get_id()
{
  return _id;
}
