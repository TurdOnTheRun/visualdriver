/*
  Channel.cpp - Library for controlling Channel.
  Created by Maximilian Weber, Dezember 25, 2020.
*/

#include "Arduino.h"
#include "Channel.h"
#include "Setting.h"
#include <math.h>

Channel::Channel()
{
  _channel = nullptr;
  _setting = nullptr;
  for(byte i=0; i<EFFECTSPERCHANNEL; i++){
    _effects[i] = nullptr;
  }
}

Channel::Channel(byte staticvalue)
{
  _isstatic = true;
  _staticvalue = staticvalue;
}

Channel::Channel(Setting* setting, Channel* channel)
{
  _channel = channel;
  _setting = setting;
  for(byte i=0; i<EFFECTSPERCHANNEL; i++){
    _effects[i] = nullptr;
  }
}

void Channel::set_setting(Setting* setting)
{
  _setting = setting;
}

void Channel::set_channel(Channel* channel)
{
  _channel = channel;
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

byte Channel::get_state(unsigned long now, byte lightid){
  if(_isstatic == true){
    return _staticvalue;
  }
  else if(_setting != nullptr){
    _newstate = _setting->get_state(now, lightid);
  }
  else if(_channel != nullptr){
    _newstate = _channel->get_state(now, lightid);
  }
  else{
    _newstate = 0;
  }
  for(byte i=0; i<EFFECTSPERCHANNEL; i++){
    if(_effects[i] != nullptr){
      _newstate = _effects[i]->get_state(now, lightid, _newstate);
    }
  }
  return _newstate;
}