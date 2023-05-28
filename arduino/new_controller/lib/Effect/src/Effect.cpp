/*
  Effect.cpp - Library for controlling Effect.
  Created by Maximilian Weber, April 2, 2023.
*/

// #include "Arduino.h"
#include "Effect.h"
#include "Controlls.h"
#include "Channel.h"
#include <math.h>

Effect::Effect(){
  _type = EFFECT_NONE;
}
Effect::Effect(byte type, Channel* amplitude, Channel* steptime, byte set1, byte set2, byte set3, byte set4, byte set5, byte set6)
{
  _type = type;
  _amplitude = amplitude;
  _steptime = steptime;
  _set1 = set1;
  _set2 = set2;
  _set3 = set3;
  _set4 = set4;
  _set5 = set5;
  _set6 = set6;

  switch(_type) {
    case EFFECT_STROBE: 
    case EFFECT_PERLIN: {
      _direction = -1;
      if(_set1){
        _steptimefactor = _set1;
      }
    } break;
  }
}

byte Effect::get_state(unsigned long now, byte lightid, byte state)
{
  if(_laststep == 0){
    _laststep = now;
    return state;
  }
  if(_type == EFFECT_NONE){
    return state;
  }
  _passed = now - _laststep;
  _newsteptime = ((unsigned int) _steptime->get_state(now,lightid)) * _steptimefactor;
  if(_newsteptime == 0){
    _newsteptime = 1;
  }
  _newamplitude = (((float) _amplitude->get_state(now,lightid)) / 100.0f);
  // If step
  if (_passed >= _newsteptime){
    switch(_type) {
      case EFFECT_UPVIBRATO: {
        _position = _position + _vibratostepangle * _passed/_newsteptime;
        // if(_position > 2 * M_PI){
        //   _position = _position - (2 * M_PI);
        // }
        _delta = _upvibrato(_position) * _newamplitude;
      } break;
      case EFFECT_DOWNVIBRATO: {
        _position = _position + _vibratostepangle * _passed/_newsteptime;
        // if(_position > 2 * M_PI){
        //   _position = _position - (2 * M_PI);
        // }
        _delta = _downvibrato(_position) * _newamplitude;
      } break;
      case EFFECT_UPDOWNVIBRATO: {
        _position = _position + _vibratostepangle * _passed/_newsteptime;
        // if(_position > 2 * M_PI){
        //   _position = _position - (2 * M_PI);
        // }
        _delta = _updownvibrato(_position) * _newamplitude;
      } break;
      case EFFECT_STROBE: {
        _on = !_on;
        _delta = _strobe(lightid);
      } break;
      case EFFECT_PERLIN: {
        _position = _position + _passed/_newsteptime;
        if(_position >= PERLIN_SIZE){
          _position = _position - PERLIN_SIZE;
        }
        _delta = _perlin_calculate() * _newamplitude;
        _direction = _get_direction(lightid);
      } break;
    }
    _laststep = now;
  } else {
    // In case no step has passed
    // Covers multisettings
    switch(_type) {
      case EFFECT_STROBE: {
        _delta = _strobe(lightid);
      } break;
      case EFFECT_PERLIN: {
        _direction = _get_direction(lightid);
      } break;
    }
  }
  _newstate = (int) round(state + (state * _delta * _direction));
  if(_newstate > 100){
    _newstate = 100;
  }
  else if(_newstate < 0){
    _newstate = 0;
  }
  return lowByte(_newstate);
}

float Effect::_strobe(byte lightid)
{
  if(_on){
    // If lightbit is 0 _on means on
    if(bitRead(_set2, lightid)){
      return 0.0f;
    } else {
      return _newamplitude;
    };
  } else {
    if(bitRead(_set2, lightid)){
      return _newamplitude;
    } else {
      return 0.0f;
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

float Effect::_perlin_calculate(){
  return (float) pgm_read_float(&PERLIN_NOISE[(unsigned int) _position]);
}

int Effect::_get_direction(byte lightid){
  // If lightbit is 0 direction is -1
  if(bitRead(_set3, lightid)){
    return 1;
  } else {
    return -1;
  };
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
