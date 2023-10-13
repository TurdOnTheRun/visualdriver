/*
  Setting.cpp - Library for controlling Setting.
  Created by Maximilian Weber, April 2, 2023.

  Types:
  1 - 9 - Static Types
  10-19 - Linear Types
  20-29 - Bezier Types
*/

#include "Arduino.h"
#include "Setting.h"
#include "Controlls.h"
#include "Channel.h"
#include <math.h>

Setting::Setting()
{
  _type = SETTING_STATIC;
  _state = 0;
}
Setting::Setting(byte type, byte set1, byte set2, byte set3, byte set4, byte set5, byte set6)
{
  _type = type;

  //_state must be set for all types
  switch(_type) {
    
    case SETTING_STATIC: {
      _state = set1;
    } break;

    case SETTING_SINGULARFLASH: {
      //set1: start state
      //set2: to state
      //set3: flash time
      _state = set1;
      _state2 = set2;
      _steptime = set3;
      if(_steptime == 0){
        _state = _state2;
        _type = SETTING_STATIC;
      }
    } break;

    case SETTING_SINGULARBURST: {
      //set1: on state
      //set2: off state
      //set3: on time (first steptime)
      //set4: off time
      //set5: amount of times
      _state = set1;
      _state1 = set1;
      _state2 = set2;
      _steptime = set3;
      //Steptime when off
      _setA = set4;
      //Amount of Ons
      _setB = set5;
    } break;

    case SETTING_SINGULARLINEAR: {
      //set1: start state
      //set2: to state
      //set3: steptime
      _state = set1;
      _state1 = set1;
      _state2 = set2;
      _steptime = set3;
      if(_steptime == 0){
        _state = _state2;
        _type = SETTING_STATIC;
      }
    } break;

    case SETTING_SINGULARBEZIER: {
      //set1: start state
      //set2: to state
      //set3: steptime
      //set4: decisteps
      //set5: y1 of bezier input
      //set6: y2 of bezier input
      _state = set1;
      _state1 = set1;
      _state2 = set2;
      _steptime = set3;
      //Decisteps
      _intervalsteps = (unsigned int) set4*10;
      //Y1
      _setA = set5;
      //Y2
      _setB = set6;
      if(_steptime == 0){
        _state = _state2;
        _type = SETTING_STATIC;
      }
    } break;
  }
}

Setting::Setting(byte type, Channel* channel1, Channel* channel2, Channel* channel3, Channel* channel4)
{
  _type = type;

  //_state must be set for all types
  switch(_type) {
    
    case SETTING_SINWAVE: {
      //channel1 --> _channelA: from state
      //channel2 --> _channelB: to state
      //channel3 --> _channelC: steptime
      //channel4 --> _channelD: decisteps
      _channelA = channel1;
      _channelB = channel2;
      _channelC = channel3;
      _channelD = channel4;
      _state = _channelA->get_state();
      _state1 = _state;
      _state2 = _channelB->get_state();
      _steptime = _channelC->get_state();
      _intervalsteps = (unsigned int) _channelD->get_state() * 10; // decisteps per interval. decisteps per change from _state1 to _state2. decisteps per PI.
      _i = 3.0f * M_PI / 2; //_i to make wave start at _state
      if(_steptime == 0){
        _steptime = 1;
      }
    } break;
  }
}

// Returns the last calculated state
byte Setting::get_state()
{
  return _state;
}

// Returns the newly calculated state for now
byte Setting::get_state(unsigned long now)
{
  if(_laststep == 0){
    _laststep = now;
    return _state;
  }
  if(_laststep == now){
    return _state;
  }
  if(_type == SETTING_STATIC){
    return _state;
  }
  else{

    // Continuous settings must update their Channel inputs
    if(_type >= SETTING_SINGULAR_DIVIDER){
      switch(_type){
        case SETTING_SINWAVE: {
          _update_sin_inputs(now);
        } break;
      }
    }
    
    _steps = (unsigned int) (now - _laststep)/_steptime;

    if (_steps == 0){
      // If _steps == 0,  state remains the same
      return _state;
    } 
    else {
      //calculated at the start because some effects change _steptime and none need _laststep  
      _laststep = _laststep + (_steps * _steptime);

      switch(_type) {
        case SETTING_SINGULARFLASH: {
          _state = _state2;
          _type = SETTING_STATIC;
        } break;

        case SETTING_SINGULARBURST: {
          // _setB counts the remaining bursts
          if(_setB == 0){
            _type = SETTING_STATIC;
            break;
          }
          if(_state == _state1){
            _state = _state2;
            _setB -= 1;
          } else {
            _state = _state1;
          }
          // switch between on time and off time
          _setC = _steptime;
          _steptime = _setA;
          _setA = _setC;
        } break;

        case SETTING_SINGULARLINEAR: {
                
          // If it is getting brighter
          if(rising()){
            
            _newstate = ((int)_state) + _steps;
            
            if(_newstate >= _state2 || _newstate > 100){
              _state = _state2;
              _type = SETTING_STATIC;
            } else {
              _state = lowByte(_newstate);
            }
          // If it is getting dimmer
          } else {
            
            _newstate = ((int)_state) - _steps;
            
            if (_newstate <= _state2 || _newstate < 0){
              _state = _state2;
              _type = SETTING_STATIC;
            } else {
              _state = lowByte(_newstate);
            }
          }
        } break;

        // case BEZIERAPPEARFLASH: --> use fall through mechanic: https://stackoverflow.com/questions/4704986/switch-statement-using-or
        case SETTING_SINGULARBEZIER: {
          //  Bezier Dimming & Direct to Bezier
      
          _intervalstep = _intervalstep + _steps;
          
          if(rising()){
            
            if(_intervalstep >= _intervalsteps){
              _state = _state2;
              if(_type == SETTING_SINGULARBEZIER){
                _type = SETTING_STATIC;
              }
              // elif BEZIERAPPEARFLASH{}
              // if(_set5 > 0){
              //   _steptime = _set5;
              //   _tostate = 0;
              //   _type = 4;
              // }
            } else {
              _bz = bezier(_intervalstep);
              _newstate = (int) round(_state1 + _bz * (_state2 - _state1));
              _state = lowByte(_newstate);
            }
            
          } else {
            
            if (_intervalstep >= _intervalsteps){
              _state = _state2;
              _type = SETTING_STATIC;
            } else {
              _bz = bezier(_intervalstep);
              _newstate = (int) round(_state1 - _bz * (_state1 - _state2));
              _state = lowByte(_newstate);
            }
          }
        } break;

        case SETTING_SINWAVE: {
          //  Sin Wave
          _update_sin();
          _set_state_from_newstate();
        } break;
      }
      return _state;
    }
  }
}

float Setting::lerp(float n1, float n2, float perc)
{
  _diff = n2 - n1;
  return n1 + ( _diff * perc );
}

float Setting::bezier(unsigned int step)
{ 
  _i = (1.0/_intervalsteps) * step;

  // The Green Lines
  _ya = lerp( 0 , _setA , _i );
  _yb = lerp( _setA , _setB , _i );
  _yc = lerp( _setB , 100 , _i );

  // The Blue Line
  _ym = lerp( _ya , _yb , _i );
  _yn = lerp( _yb , _yc , _i );

  // The Black Dot
  _y = lerp( _ym , _yn , _i ) / 100;
  return _y;
}

void Setting::_update_sin_inputs(unsigned long now)
{
  //_channelA: crest state
  //_channelB: trough state
  //_channelC: steptime
  //_channelD: decisteps
  _state1 = _channelA->get_state(now);
  _state2 = _channelB->get_state(now);
  _steptime = _channelC->get_state(now);
  _intervalsteps = (unsigned int) _channelD->get_state(now) * 10; // decisteps per interval. decisteps per change from _state1 to _state2. decisteps per PI.
  if(_steptime == 0){
    _steptime = 1;
  }
}

void Setting::_update_sin()
{
  _i = _i + (float) (M_PI / _intervalsteps) * _steps;
  _y = _state1 + ((sin(_i) + 1)/2) * (_state2-_state1);
  _newstate = (int) _y;
}

void Setting::_set_state_from_newstate()
{
  if(_newstate < 0){
    _state=0;
  }
  else if(_newstate > 100){
    _state = 100;
  }
  else{
    _state = lowByte(_newstate);
  }
}

bool Setting::changing()
{
  return !(_state == _state2);
}
    
bool Setting::rising()
{
  return (_state < _state2);
}

byte Setting::get_type()
{
  return _type;
}
