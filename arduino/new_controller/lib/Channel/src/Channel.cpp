/*
  Channel.cpp - Library for controlling Channel.
  Created by Maximilian Weber, Dezember 25, 2020.
*/

#include "Arduino.h"
#include "Channel.h"
#include "Setting.h"
#include "Effect.h"
#include <math.h>

Channel::Channel()
{
  _channel = nullptr;
  _setting = nullptr;
  for(byte i=0; i<EFFECTSPERCHANNEL; i++){
    _effects[i] = nullptr;
  }
}

Channel::Channel(byte staticstate)
{
  _isstatic = true;
  _state = staticstate;
  for(byte i=0; i<EFFECTSPERCHANNEL; i++){
    _effects[i] = nullptr;
  }
}

void Channel::set_setting(Setting* setting)
{
  _setting = setting;
  _channel = nullptr;
  _isstatic = false;
  _state = setting->get_state();
}

void Channel::set_channel(Channel* channel)
{
  _channel = channel;
  _setting = nullptr;
  _isstatic = false;
  _state = channel->get_state();
}

void Channel::set_static(byte staticstate)
{
  _channel = nullptr;
  _setting = nullptr;
  _isstatic = true;
  _state = staticstate;
}

void Channel::add_effect(Effect* effect, byte index)
{ 
  if(index < EFFECTSPERCHANNEL){
    _effects[index] = effect;
  }
}

void Channel::remove_effect(byte index)
{
  if(index < EFFECTSPERCHANNEL){
    _effects[index] = nullptr;
  }
}

void Channel::remove_effects()
{
  for(byte i=0; i<EFFECTSPERCHANNEL; i++){
    _effects[i] = nullptr;
  }
}

// Returns the last calculated state
byte Channel::get_state()
{
  return _state;
}

// Returns the newly calculated state for now
byte Channel::get_state(unsigned long now){
  if(_isstatic == true){
    _newstate = _state;
  }
  else if(_setting != nullptr){
    _newstate = _setting->get_state(now);
  }
  else if(_channel != nullptr){
    _newstate = _channel->get_state(now);
  }
  else{
    _newstate = _state;
  }
  for(byte i=0; i<EFFECTSPERCHANNEL; i++){
    if(_effects[i] != nullptr){
      _newstate = _effects[i]->get_state(now, _newstate);
    }
  }
  _state = _newstate;
  return _state;
}
