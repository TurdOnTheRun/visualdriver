/*
  Light.cpp - Library for controlling Light.
  Created by Maximilian Weber, Dezember 25, 2020.
*/

#include "Arduino.h"
#include "Light.h"
#include <math.h>

Light::Light(byte id, byte pin, Setting* setting)
{
  _id = id;
  _pin = pin;
  _setting = setting;
  _setting->usercount_up();
}

void Light::init()
{
  pinMode(_pin, OUTPUT);
  set_pin_frequency();
  for(byte i=0; i<EFFECTSPERLIGHT; i++){
    _effects[i] = NULL;
  }
}

void Light::set_pin_frequency()
{
  //only necessary for uno
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


void Light::set_setting(Setting* setting)
{
  _setting->usercount_down();
  _setting = setting;
  _setting->usercount_up();
}

void Light::add_effect(Effect* effect)
{
  for(byte i=0; i<EFFECTSPERLIGHT; i++){
    if(_effects[i] == NULL){
      effect->usercount_up();
      _effects[i] = effect;
      break;
    }
  }
}

void Light::remove_effect(Effect* effect)
{
  for(byte i=0; i<EFFECTSPERLIGHT; i++){
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

void Light::remove_effects()
{
  for(byte i=0; i<EFFECTSPERLIGHT; i++){
     if(_effects[i] != NULL){
      _effects[i]->usercount_down();
      _effects[i] = NULL;
     }
  }
}

void Light::update(unsigned long now)
{
  _newstate = _setting->get_state(now, _id);
  for(byte i=0; i<EFFECTSPERLIGHT; i++){
    if(_effects[i] != NULL){
      _newstate = _effects[i]->get_state(now, _id, _newstate);
    }
  }
  set_pinstate();
}

byte Light::get_id()
{
  return _id;
}
