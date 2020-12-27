/*
  Light.cpp - Library for controlling Light.
  Created by Maximilian Weber, Dezember 25, 2020.
*/

#include "Arduino.h"
#include "Light.h"

Light::Light(byte id, byte pin)
{
  _pin = pin;
  _id = id;
}

void Light::init()
{
  pinMode(_pin, OUTPUT);
}

void Light::setstate(byte newstate)
{
  analogWrite(_pin, newstate);
  _state = newstate;
  _laststep = millis();
}

void Light::update()
{
  if (changing()){
    
    unsigned long passed = millis() - _laststep;
    if (passed < _steptime){
      return;
    }
  
    if(_type != 2){
      //  Not strobe
      int steps = (int) round(passed/_steptime);
  
      int newstate;
      
      if (rising()){
        
        newstate = ((int)_state) + steps;
        
        if (newstate >= _tostate || newstate > 255){
          setstate(_tostate);
        } else {
          setstate(lowByte(newstate));
        }
        
      } else {
        
        newstate = ((int)_state) - steps;
        
        if (newstate <= _tostate || newstate < 0){
          setstate(_tostate);
        } else {
          setstate(lowByte(newstate));
        }
        
      }
    } 
    else {
      //  Strobe
      if(_state == 0){
        setstate(_tostate);
        _tostate = 0;
      } else {
        _tostate = _state;
        setstate(0);
      }
    }
  }
}

void Light::setto(byte type, byte tostate, byte steptime)
{
  if(type == 0){
    setstate(tostate);
    _tostate = tostate;
  }
  else if(type == 1){
    if(steptime == 0){
      setstate(tostate);
      _tostate = tostate;
    } else {
      _steptime = steptime;
      _tostate = tostate;
      _laststep = millis();
    }
  }
  else if(type == 2){
    if(_state == tostate){
      setstate(0);
      _tostate = tostate;
    } else {
      setstate(tostate);
      _tostate = 0;
    }
    _steptime = steptime;
  }
  _type = type;
}

bool Light::changing()
{
  return !(_state == _tostate);
}
    
bool Light::rising()
{
  return (_state < _tostate);
}

byte Light::getid()
{
  return _id;
}
