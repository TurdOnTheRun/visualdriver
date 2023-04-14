/*
  LightEffect.cpp - Library for controlling LightEffect.
  Created by Maximilian Weber, April 2, 2023.
*/

// #include "Arduino.h"
#include "LightEffect.h"
#include <math.h>

LightEffect::LightEffect(){}
LightEffect::LightEffect(byte type, byte amplitude, byte steptime, byte set1, byte set2, byte set3, byte set4, byte set5, byte set6)
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

void LightEffect::init(unsigned long now)
{
  switch(_type) {
    case STROBE: {
      if(_set1){
        _amplitude = -1 * _amplitude * _set1;
      } else {
        _amplitude = -1 * _amplitude;
      }
    } break;
  }
  _laststep = now;
}

byte LightEffect::get_state(unsigned long now, byte lightid, byte state)
{
  _passed = now - _laststep;
  // If step
  if (_passed >= _steptime){
    switch(_type) {
      case UPVIBRATO: {
        _vibratoangle = _vibratoangle + _vibratostepangle * _passed/_steptime;
        // if(_vibratoangle > 2 * M_PI){
        //   _vibratoangle = _vibratoangle - (2 * M_PI);
        // }
        _delta = _upvibrato(_vibratoangle) * _amplitude;
      } break;
      case DOWNVIBRATO: {
        _vibratoangle = _vibratoangle + _vibratostepangle * _passed/_steptime;
        // if(_vibratoangle > 2 * M_PI){
        //   _vibratoangle = _vibratoangle - (2 * M_PI);
        // }
        _delta = _downvibrato(_vibratoangle) * _amplitude;
      } break;
      case UPDOWNVIBRATO: {
        _vibratoangle = _vibratoangle + _vibratostepangle * _passed/_steptime;
        // if(_vibratoangle > 2 * M_PI){
        //   _vibratoangle = _vibratoangle - (2 * M_PI);
        // }
        _delta = _updownvibrato(_vibratoangle) * _amplitude;
      } break;
      case STROBE: {
        _on = !_on;
        _set_strobe_delta(lightid);
      } break;
    }
    _laststep = now;
  } else {
    switch(_type) {
      case STROBE: {
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

void LightEffect::_set_strobe_delta(byte lightid)
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

float LightEffect::_updownvibrato(float angle)
{ 
  return sin(angle);
}

float LightEffect::_upvibrato(float angle)
{ 
  return (cos(angle) * (-1) + 1)/2;
}

float LightEffect::_downvibrato(float angle)
{ 
  return (cos(angle)-1)/2;
}

byte LightEffect::get_type()
{
  return _type;
}

void LightEffect::usercount_up()
{
  _usercount += 1;
}

void LightEffect::usercount_down(){
  _usercount -= 1;
}

boolean LightEffect::is_unused(){
  return _usercount < 1;
}