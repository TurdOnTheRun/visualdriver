/*
  Light.cpp - Library for controlling Light.
  Created by Maximilian Weber, Dezember 25, 2020.
*/

#include "Arduino.h"
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
  for(byte i; i<EFFECTSPERLIGHT; i++){
    _effects[i] = NULL;
  }
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

void Light::add_effect(LightEffect* effect)
{
  for(byte i; i<EFFECTSPERLIGHT; i++){
    if(_effects[i] == NULL){
      effect->usercount_up();
      _effects[i] = effect;
    }
  }
}

void Light::remove_effect(LightEffect* effect)
{
  for(byte i; i<EFFECTSPERLIGHT; i++){
    if(_effects[i] == effect){
      effect->usercount_down();
      _effects[i] = NULL;
    }
  }
}

void Light::remove_effect(byte index)
{
  if(index < EFFECTSPERLIGHT){
    if(_effects[index] != NULL){
      _effects[index]->usercount_down();
      _effects[index] = NULL;
    }
  }
}

void Light::update(unsigned long now)
{
  _newstate = _setting->get_state(now, _id);
  for(byte i=0; i<EFFECTSPERLIGHT; i++){
    if(_effects[i] != NULL){
      Serial.println(123);
      _newstate = _effects[i]->get_state(now, _id, _newstate);
    }
  }
  set_pinstate();
}

byte Light::get_id()
{
  return _id;
}
