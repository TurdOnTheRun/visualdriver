/*
  Light.cpp - Library for controlling Light.
  Created by Maximilian Weber, Dezember 25, 2020.
*/

#include "Arduino.h"
#include "Motor.h"
#include <math.h>

Motor::Motor(byte LPWM_pin, byte RPWM_pin)
{
  _LPWM_pin = LPWM_pin;
  _RPWM_pin = RPWM_pin;
}

void Motor::init()
{
  pinMode(_LPWM_pin, OUTPUT);
  pinMode(_RPWM_pin, OUTPUT);
  _OUT_pin = _LPWM_pin;
  _NOTOUT_pin = _RPWM_pin;
}

void Motor::set_state()
{
  if(_state != lowByte(_newstate)){
    pin_write();
    _state = lowByte(_newstate);
    if (_state != 0){
      _stopped = false;
    } else {
      _stopped = true;
    }
  }
}

void Motor::pin_write()
{
  analogWrite(_NOTOUT_pin, 0);
  analogWrite(_OUT_pin, lowByte(_newstate));
}

void Motor::set_to(byte tostate, byte steptime, unsigned long now)
{
  if (_changingDirection){
    return;
  }
  if (steptime < 20) {
    byte difference;
    if (_state > tostate) {
      difference = _state-tostate;
    } else {
      difference = tostate-_state;
    }
    if (difference > MAXIMAL_SPEED_DIFFERENCE){
      steptime = 20;
    }
  }
  if (tostate > MAXIMUM_SPEED){
    tostate = MAXIMUM_SPEED;
  }
  _tostate = tostate;
  _steptime = steptime;
  _laststep = now;
}

void Motor::update(unsigned long now)
{
  if (changing()){
    
    unsigned long passed = now - _laststep;
    int steps;
    
    if (passed < _steptime){
      return;
    } else {
      steps = (int) round(passed/_steptime);
    }
    
    if (rising()){
      
      _newstate = ((int)_state) + steps;
      
      if (_newstate >= _tostate || _newstate > MAXIMUM_SPEED){
        _newstate = _tostate;
      }
      
    } else {
      
      _newstate = ((int)_state)-steps;
      
      if (_newstate <= _tostate || _newstate < 0){
         _newstate = _tostate;
      }

    }
    set_state();
    _laststep = now;
  } else if (_changingDirection && _stopped) {
    byte TEMP_pin = _OUT_pin;
    _OUT_pin = _NOTOUT_pin;
    _NOTOUT_pin = TEMP_pin;
    _changingDirection = false;
    set_to(_savestate, 20, now);
  }
}

void Motor::change_direction(unsigned long now) {
  _savestate = _state;
  _tostate = 0;
  _steptime = 20;
  _changingDirection = true;
  _laststep = now;
}

bool Motor::rising() {
  return (_state < _tostate);
}

bool Motor::changing() {
  return !(_state == _tostate);
}
