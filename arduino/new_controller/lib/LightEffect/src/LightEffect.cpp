/*
  LightEffect.cpp - Library for controlling LightEffect.
  Created by Maximilian Weber, April 2, 2023.

  Types:
  10-19 - Static Types
  20-29 - Linear Types
  30-39 - Bezier Types
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

void LightEffect::init()
{
  switch(_type) {
    case MILLISTROBE: {
      _amplitude = -1 * _amplitude;
    } break;
    case DECISTROBE: {
      _amplitude = -1 * _amplitude;
      _steptime = _steptime * 10;
    } break;
  }
}

byte LightEffect::get_state(unsigned long now, byte lightid, byte state)
{
  if(_laststep == now && (_type==UPDOWNVIBRATO || _type==DOWNVIBRATO || _type==UPVIBRATO)){
    // no need to recalculate delta
  }
  else if(_laststep == 0){
    _laststep = now;
    _delta = 0.0;
  }
  else{
    _passed = now - _laststep;
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
        case MILLISTROBE:
        case DECISTROBE: {
          if(_on){
            // If lightbit is 0 _on means on
            if(bitRead(_set1, lightid)){
              _delta = 0.0;
            } else {
              _delta = _amplitude;
            };
            _on = false;
          } else {
            if(bitRead(_set1, lightid)){
              _delta = _amplitude;
            } else {
              _delta = 0.0;
            }
            _on = true;
          }
        } break;
      }
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
