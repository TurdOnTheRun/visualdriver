/*
  Effect.cpp - Library for controlling Effect.
  Created by Maximilian Weber, April 2, 2023.
*/

// #include "Arduino.h"
#include "Effect.h"
#include "Controlls.h"
#include <math.h>

Effect::Effect(){}
Effect::Effect(byte type, byte amplitude, byte steptime, byte set1, byte set2, byte set3, byte set4, byte set5, byte set6)
{
  _type = type;
  _amplitude = (float) amplitude / 100;
  _steptime = (int) steptime;
  _set1 = set1;
  _set2 = set2;
  _set3 = set3;
  _set4 = set4;
  _set5 = set5;
  _set6 = set6;
}

void Effect::init(unsigned long now)
{
  switch(_type) {
    case EFFECT_STROBE: {
      if(_set1){
        _amplitude = -1 * _amplitude * _set1;
      } else {
        _amplitude = -1 * _amplitude;
      }
    } break;
  }
  _laststep = now;
}

byte Effect::get_state(unsigned long now, byte lightid, byte state)
{
  if(_laststep == 0){
    init(now);
    return state;
  }
  _passed = now - _laststep;
  // If step
  if (_passed >= _steptime){
    switch(_type) {
      case EFFECT_UPVIBRATO: {
        _vibratoangle = _vibratoangle + _vibratostepangle * _passed/_steptime;
        // if(_vibratoangle > 2 * M_PI){
        //   _vibratoangle = _vibratoangle - (2 * M_PI);
        // }
        _delta = _upvibrato(_vibratoangle) * _amplitude;
      } break;
      case EFFECT_DOWNVIBRATO: {
        _vibratoangle = _vibratoangle + _vibratostepangle * _passed/_steptime;
        // if(_vibratoangle > 2 * M_PI){
        //   _vibratoangle = _vibratoangle - (2 * M_PI);
        // }
        _delta = _downvibrato(_vibratoangle) * _amplitude;
      } break;
      case EFFECT_UPDOWNVIBRATO: {
        _vibratoangle = _vibratoangle + _vibratostepangle * _passed/_steptime;
        // if(_vibratoangle > 2 * M_PI){
        //   _vibratoangle = _vibratoangle - (2 * M_PI);
        // }
        _delta = _updownvibrato(_vibratoangle) * _amplitude;
      } break;
      case EFFECT_STROBE: {
        _on = !_on;
        _set_strobe_delta(lightid);
      } break;
    }
    _laststep = now;
  } else {
    switch(_type) {
      case EFFECT_STROBE: {
        _set_strobe_delta(lightid);
      } break;
    }
  }
  _newstate = (int) round(state + state * _delta);
  if(_newstate > 100){
    _newstate = 100;
  }
  else if(_newstate < 0){
    _newstate = 0;
  }
  return lowByte(_newstate);
}

void Effect::_set_strobe_delta(byte lightid)
{
  if(_on){
    // If lightbit is 0 _on means on
    if(bitRead(_set2, lightid)){
      _delta = 0.0;
    } else {
      _delta = _amplitude;
    };
  } else {
    if(bitRead(_set2, lightid)){
      _delta = _amplitude;
    } else {
      _delta = 0.0;
    }
  }
}

float Effect::_updownvibrato(float angle)
{ 
  return sin(angle);
}

float Effect::_upvibrato(float angle)
{ 
  return (cos(angle) * (-1) + 1)/2;
}

float Effect::_downvibrato(float angle)
{ 
  return (cos(angle)-1)/2;
}

byte Effect::get_type()
{
  return _type;
}

void Effect::usercount_up()
{
  _usercount += 1;
}

void Effect::usercount_down(){
  _usercount -= 1;
}

boolean Effect::is_unused(){
  return _usercount < 1;
}
