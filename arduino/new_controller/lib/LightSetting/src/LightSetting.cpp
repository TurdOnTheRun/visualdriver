/*
  LightSetting.cpp - Library for controlling LightSetting.
  Created by Maximilian Weber, April 2, 2023.

  Types:
  1 - 9 - Static Types
  10-19 - Linear Types
  20-29 - Bezier Types
*/

// #include "Arduino.h"
#include "LightSetting.h"
#include <math.h>

LightSetting::LightSetting(){}
LightSetting::LightSetting(byte type, byte state1, byte state2, byte steptime, byte set1, byte set2, byte set3, byte set4, byte set5)
{
  _type = type;
  _state1 = state1;
  _state2 = state2;
  _steptime = steptime;
  _set1 = set1;
  _set2 = set2;
  _set3 = set3;
  _set4 = set4;
  _set5 = set5;
}

void LightSetting::init(unsigned long now)
{
  switch(_type) {
    case STATICLIGHT: {
      _state = _state1;
    } break;

    case STATICFLASH: {
      // Goes from state1 to state2 after steptime
      if(_steptime == 0){
        _state = _state2;
        _type = STATICLIGHT;
      } else {
        _state = _state1;
      }
    } break;

    case STATICMACHINE: {
      //Goes from state1 to state2 after steptime, stays at state2 for set1, then returns to state1. Repeats set2 times
      _state = _state1;
    } break;

    case LINEARDIMM: {
      // Goes from state1 to state2 taking steptime for each increment
      if(_steptime == 0){
        _state = _state2;
        _type = STATICLIGHT;
      } else {
        _state = _state1;
      }
      // _set1 = 0;
    } break;

    case BEZIERDIMM: {
      // Bezier Dimm from state1 to state2
      if(_steptime == 0){
        _state = _state2;
        _type = STATICLIGHT;
      } else {
        _bezierstep = 0;
        _beziersteps = (unsigned int) _set1/0.1;
        _state = _state1;
      }
    } break;
  }
  _laststep = now;
}

byte LightSetting::get_state(unsigned long now, byte lightid)
{
  if(_laststep == now){
    return _state;
  }
  if(_type == STATICLIGHT){
    return _state;
  }
  else{
    
    _passed = now - _laststep;

    if (_passed >= _steptime){

      switch(_type) {
        case STATICFLASH: {
          _state = _state2;
          _type = STATICLIGHT;
        } break;

        case STATICMACHINE: {
          if(_set2 == 0){
            _type = STATICLIGHT;
            break;
          }
          if(_state == _state1){
            _state = _state2;
            _set2 -= 1;
          } else {
            _state = _state1;
          }
          _set3 = _steptime;
          _steptime = _set1;
          _set1 = _set3;
        } break;
        // case LINEARAPPEARFLASH: --> use fall through mechanic: https://stackoverflow.com/questions/4704986/switch-statement-using-or
        case LINEARDIMM: {
          _steps = (int) round(_passed/_steptime);

          if(_steps == 0){
            break;
          }
                
          // If it is getting brighter
          if(rising()){
            
            _newstate = ((int)_state) + _steps;
            
            if(_newstate >= _state2 || _newstate > 100){
              _state = _state2;
              if(_type == LINEARDIMM){
                _type = STATICLIGHT;
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
              _type = STATICLIGHT;
            } else {
              _state = lowByte(_newstate);
            }
            
          }
        } break;

        // case BEZIERAPPEARFLASH: --> use fall through mechanic: https://stackoverflow.com/questions/4704986/switch-statement-using-or
        case BEZIERDIMM: {
          //  Bezier Dimming & Direct to Bezier
          _steps = (int) round(_passed/_steptime);

          if(_steps == 0){
            break;
          }
      
          _bezierstep = _bezierstep + _steps;
          
          if(rising()){
            
            if(_bezierstep >= 100){
              _state = _state2;
              if(_type == BEZIERDIMM){
                _type = STATICLIGHT;
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
            
            if (_bezierstep >= 100){
              _state = _state2;
              _type = STATICLIGHT;
            } else {
              _bz = bezier(_bezierstep);
              _newstate = (int) round(_state1 - _bz * (_state1 - _state2));
              _state = lowByte(_newstate);
            }
          }
        } break;
      }
      _laststep = now;
      return _state;
    } else {
      // If _passed < _steptime, state remains the same
      return _state;
    }
  }
}

void LightSetting::set_state(unsigned long now, byte newstate)
{
  if(newstate > 100){
    newstate = 100;
  }
  _state = newstate;
  _laststep = now;
}

float LightSetting::lerp(float n1, float n2, float perc)
{
  _diff = n2 - n1;
  return n1 + ( _diff * perc );
}

float LightSetting::bezier(byte step)
{ 
  // There are a total of 100 steps
  _i = _beziersteps * step;

  // The Green Lines
  _ya = lerp( 0 , _set2 , _i );
  _yb = lerp( _set2 , _set3 , _i );
  _yc = lerp( _set3 , 100 , _i );

  // The Blue Line
  _ym = lerp( _ya , _yb , _i );
  _yn = lerp( _yb , _yc , _i );

  // The Black Dot
  _y = lerp( _ym , _yn , _i ) / 100;
  return _y;
}

bool LightSetting::changing()
{
  return !(_state == _state2);
}
    
bool LightSetting::rising()
{
  return (_state < _state2);
}

byte LightSetting::get_type()
{
  return _type;
}

void LightSetting::usercount_up()
{
  _usercount += 1;
}

void LightSetting::usercount_down(){
  _usercount -= 1;
}

boolean LightSetting::is_unused(){
  return _usercount < 1;
}
