/*
  Light.cpp - Library for controlling Light.
  Created by Maximilian Weber, Dezember 25, 2020.
*/

// #include "Arduino.h"
#include "Light.h"
#include <math.h>

Light::Light(byte id, byte pin, LightSetting *setting)
{
  _id = id;
  _pin = pin;
  _setting = setting;
}

void Light::init()
{
  pinMode(_pin, OUTPUT);
}

void Light::set_pinstate(byte newstate)
{
  if(newstate > 100){
    newstate = 100;
  }
  if(_pinstate != newstate){
    analogWrite(_pin, _statemap[newstate]);
    _pinstate = newstate;
  }
}

void Light:set_setting(LightSetting *setting)
{
  _setting = setting;
}

void Light::update(unsigned long now)
{
  state = _setting->get_state(now, _id)
  // for effect in effects:
  //    state = effect.get_state(state, _id)
  set_pinstate(state);
}

byte Light::get_id()
{
  return _id;
}
