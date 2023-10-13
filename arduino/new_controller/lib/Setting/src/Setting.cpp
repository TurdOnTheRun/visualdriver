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
      _beziersteps = (unsigned int) set4/0.1;
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


byte Setting::get_state(unsigned long now, byte lightid)
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
    
    _steps = (unsigned int) (now - _laststep)/_steptime;

    if (_steps > 0){

      //calculated at the start because some effects change _steptime and none need _laststep  
      _laststep = _laststep + (_steps * _steptime);

      switch(_type) {
        case SETTING_SINGULARFLASH: {
          _state = _state2;
          _type = SETTING_STATIC;
        } break;

        case SETTING_SINGULARBURST: {
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
          _setC = _steptime;
          _steptime = _setA;
          _setA = _setC;
        } break;
        // case LINEARAPPEARFLASH: --> use fall through mechanic: https://stackoverflow.com/questions/4704986/switch-statement-using-or
        case SETTING_SINGULARLINEAR: {
                
          // If it is getting brighter
          if(rising()){
            
            _newstate = ((int)_state) + _steps;
            
            if(_newstate >= _state2 || _newstate > 100){
              _state = _state2;
              if(_type == SETTING_SINGULARLINEAR){
                _type = SETTING_STATIC;
              }
              // // else For Lightning Appear (6)
              // // Set how long light should stay at _tostate
              // if(_set1 > 0){
              //   _steptime = _set1;
              //   _tostate = 0;
              //   _type = 4;
              // }
            } else {
              _state = lowByte(_newstate);
            }
          // If it is getting less bright
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
      
          _bezierstep = _bezierstep + _steps;
          
          if(rising()){
            
            if(_bezierstep >= _beziersteps){
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
              _bz = bezier(_bezierstep);
              _newstate = (int) round(_state1 + _bz * (_state2 - _state1));
              _state = lowByte(_newstate);
            }
            
          } else {
            
            if (_bezierstep >= _beziersteps){
              _state = _state2;
              _type = SETTING_STATIC;
            } else {
              _bz = bezier(_bezierstep);
              _newstate = (int) round(_state1 - _bz * (_state1 - _state2));
              _state = lowByte(_newstate);
            }
          }
        } break;
      }
      return _state;
    } else {
      // If _steps == 0,  state remains the same
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
  // There are a total of 100 steps
  _i = (1.0/_beziersteps) * step;

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
