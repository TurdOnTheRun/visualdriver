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

byte Effect::get_state(unsigned long now, byte state)
{
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
