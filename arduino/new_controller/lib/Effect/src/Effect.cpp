/*
  Effect.cpp - Library for controlling Effect.
  Created by Maximilian Weber, April 2, 2023.
*/

#include "Arduino.h"
#include "Effect.h"
#include "Controlls.h"
#include "Channel.h"
#include <math.h>

Effect::Effect(){
  _type = EFFECT_NONE;
}
Effect::Effect(byte type, Channel* channel1)
{
  _type = type;

  switch(_type) {
    case EFFECT_NONE: {
      // Does not need any input
    } break;
    case EFFECT_INVERSE: {
      // Does not need any input
    } break;
    case EFFECT_ADD: {
      //channel1 --> _channelA: y in state = state + y
      _channelA = channel1;
    } break;
    case EFFECT_SUBTRACT: {
      //channel1 --> _channelA: y in state = state - y
      _channelA = channel1;
    } break;
    case EFFECT_ADDPERCENTAGE: {
      //channel1 --> _channelA: y in state = state + (state * y/100)
      _channelA = channel1;
    } break;
    case EFFECT_SUBTRACTPERCENTAGE: {
      //channel1 --> _channelA: y in state = state - (state * y/100)
      _channelA = channel1;
    } break;
    case EFFECT_PERCENTAGE: {
      //channel1 --> _channelA: y in state = state * y/100
      _channelA = channel1;
    } break;
  }
}

Effect::Effect(byte type, Channel* channel1, byte* sequence)
{
  _type = type;

  switch(_type) {
    case EFFECT_SEQUENCEDLIGHTSTROBE: {
      _channelA = channel1;
      _sequence = new byte[SEQUENCE_SIZE];
      memcpy(_sequence, sequence, SEQUENCE_SIZE);
      _index = 0;
    } break;
  }
}

byte Effect::get_state(unsigned long now, byte state, byte lightid)
{ 

  if(_type < EFFECT_STEPTIME_DIVIDER){
    switch(_type) {
      case EFFECT_NONE: {
        return state;
      } break;
      case EFFECT_INVERSE: {
        _newstate = 100 - state;
        return _get_state_from_newstate();
      } break;
      case EFFECT_ADD: {
        _varA = _channelA->get_state(now);
        _newstate = state + _varA;
        return _get_state_from_newstate();
      } break;
      case EFFECT_SUBTRACT: {
        _varA = _channelA->get_state(now);
        _newstate = state - _varA;
        return _get_state_from_newstate();
      } break;
      case EFFECT_ADDPERCENTAGE: {
        _varA = _channelA->get_state(now);
        _newstate = (int) (state + (state * _varA/100.0f));
        return _get_state_from_newstate();
      } break;
      case EFFECT_SUBTRACTPERCENTAGE: {
        _varA = _channelA->get_state(now);
        _newstate = (int) (state - (state * _varA/100.0f));
        return _get_state_from_newstate();
      } break;
      case EFFECT_PERCENTAGE: {
        _varA = _channelA->get_state(now);
        _newstate = (int) (state * _varA/100.0f);
        return _get_state_from_newstate();
      } break;
      default: {
        return state;
      } break;
    }
  }
  else {
    if(_laststep == 0){
      _laststep = now;
    }
    if(_laststep != now){
      _varA = _channelA->get_state(now);
      _steps = (byte) (now - _laststep)/_varA;
      // For datk boolean this is where it would be triggered
      if(_steps != 0){
        _index += _steps;
        _laststep = _laststep + (_steps * _varA) - _get_steptime_adjustment();
      }
    }
    switch(_type) {
      case EFFECT_SEQUENCEDLIGHTSTROBE: {
        if(_index >= SEQUENCE_SIZE || _sequence[_index] == 0){
          _index = 0;
        }
        if(_sequence[_index] == lightid){
          return state;
        } else{
          return 0;
        }
      } break;
    }
  }
}

byte Effect::_get_steptime_adjustment()
{
  switch(_varA) {
    case 9: {
      _fract+=NTSC_9_NUMERATOR;
    } break;
    case 17: {
      _fract+=NTSC_17_NUMERATOR;
    } break;
    case 26: {
      _fract+=NTSC_26_NUMERATOR;
    } break;
    case 34: {
      _fract+=NTSC_34_NUMERATOR;
    } break;
    case 42: {
      _fract+=NTSC_42_NUMERATOR;
    } break;
    case 51: {
      _fract+=NTSC_51_NUMERATOR;
    } break;
    case 59: {
      _fract+=NTSC_59_NUMERATOR;
    } break;
    case 67: {
      _fract+=NTSC_67_NUMERATOR;
    } break;
    default: {
      return 0;
    }
  }
}

byte Effect::_get_state_from_newstate()
{
  if(_newstate < 0){
    return 0;
  }
  else if(_newstate > 100){
    return 100;
  }
  else{
    return lowByte(_newstate);
  }
}

byte Effect::get_type()
{
  return _type;
}
