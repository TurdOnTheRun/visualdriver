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
    case EFFECT_LASTORZERO: {
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

Effect::Effect(byte type, Channel* channel1, Channel* channel2, byte set1, byte set2, byte set3, byte set4)
{
  _type = type;

  switch(_type) {
    case EFFECT_SEQUENCEDLIGHTSTROBE: {
      //channel1 --> _channelA: steptime
      //channel2 --> _channelB: darksteptime
      //set1-4   --> _sequence
      _channelA = channel1;
      _channelB = channel2;
      _steptime = _channelA->get_state();
      _varA = _channelB->get_state();
      // misusing _laststep variable before its needed
      _laststep = (static_cast<unsigned long>(set1) << 24) |
                  (static_cast<unsigned long>(set2) << 16) |
                  (static_cast<unsigned long>(set3) << 8) |
                  static_cast<unsigned long>(set4);
      do {
        _sequence[_index++] = static_cast<byte>(_laststep % 10);
        _laststep /= 10;
      } while (_laststep > 0);
      _index = 0;
      _laststep = 0;
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
      case EFFECT_LASTORZERO: {
        if(state != 0){
          _varA = state;
          return 0;
        } else {
          return _varA;
        }
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
      if(_steptime == 0){
        _laststep = now;
      } else {
        _laststep = now - (now % _steptime);
      }
    }
    if(_laststep != now){
      _steptime = _channelA->get_state(now);
      _varA = _channelB->get_state(now); //darkstep boolean

      _steps = (byte) (now - _laststep)/_steptime;

      if(_steps != 0){
        _laststep = _laststep + (_steps * _steptime) - _get_steptime_adjustment();
        _darksteptracker += _steps;
        // In case of a darkstep
        if(_darksteptracker%2 && _varA){
          return 0;
        } else {
          _index += _steps;
        }
      } else if(_darksteptracker%2 && _varA){
        return 0;
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
  switch(_steptime) {
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

  if(_fract>=NTSC_DENOMINATOR){
    _fract-=NTSC_DENOMINATOR;
    return 1;
  } else {
    return 0;
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
