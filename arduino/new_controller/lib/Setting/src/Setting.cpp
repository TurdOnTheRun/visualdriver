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

Setting::Setting(byte type, Channel* channel1, Channel* channel2, Channel* channel3, Channel* channel4, Channel* channel5, Channel* channel6)
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

    case SETTING_LINEARWAVE: {
      //channel1 --> _channelA: from state
      //channel2 --> _channelB: to state
      //channel3 --> _channelC: steptime
      _init_linear_inputs(channel1, channel2, channel3);
    } break;

    case SETTING_LINEARSAW: {
      //channel1 --> _channelA: from state
      //channel2 --> _channelB: to state
      //channel3 --> _channelC: steptime
      _init_linear_inputs(channel1, channel2, channel3);
    } break;

    case SETTING_BEZIERWAVE: {
      //channel1 --> _channelA: from state
      //channel2 --> _channelB: to state
      //channel3 --> _channelC: steptime
      //channel4 --> _channelD: decisteps
      //channel5 --> _channelE: y1
      //channel6 --> _channelF: y2
      _init_bezier_inputs(channel1, channel2, channel3, channel4, channel5, channel6);
    } break;

    case SETTING_BEZIERSAW: {
      //channel1 --> _channelA: from state
      //channel2 --> _channelB: to state
      //channel3 --> _channelC: steptime
      //channel4 --> _channelD: decisteps
      //channel5 --> _channelE: y1
      //channel6 --> _channelF: y2
      _init_bezier_inputs(channel1, channel2, channel3, channel4, channel5, channel6);
    } break;

    case SETTING_SQUAREWAVE: {
      //channel1 --> _channelA: from state
      //channel2 --> _channelB: to state
      //channel3 --> _channelC: from steptime
      //channel4 --> _channelD: to steptime
      //channel5 --> _channelE: from steptime-factor
      //channel6 --> _channelF: to steptime-factor

      _channelA = channel1;
      _channelB = channel2;
      _channelC = channel3;
      _channelD = channel4;
      _channelE = channel5;
      _channelF = channel6;

      _state = _channelA->get_state();
      _state1 = _state;
      _state2 = _channelB->get_state();
      _setA = _channelC->get_state(); //from steptime
      _setB = _channelD->get_state(); //to steptime
      _setC = _channelE->get_state(); //from steptime-factor
      _setD = _channelF->get_state(); //to steptime-factor

      // steptime-factors are set to 1 if 0
      if(_setC == 0){
        _setC = 1;
      }
      if(_setD == 0){
        _setD = 1;
      }

      _steptime = (unsigned int) _setA * _setC;
      if(_steptime == 0){
        _steptime = 1;
      }
    } break;

    case SETTING_NOISE: {
      //channel1 --> _channelA: from state
      //channel2 --> _channelB: to state
      //channel3 --> _channelC: steptime
      //channel4 --> _channelD: steptime-factor

      _channelA = channel1;
      _channelB = channel2;
      _channelC = channel3;
      _channelD = channel4;

      _state = _channelA->get_state();
      _state1 = _state;
      _state2 = _channelB->get_state();
      _setA = _channelC->get_state(); //steptime
      _setB = _channelD->get_state(); //steptime-factor

      if(_setB == 0){
        _setB = 1;
      }

      _steptime = (unsigned int) _setA * _setB;
      if(_steptime == 0){
        _steptime = 1;
      }
    } break;

    case SETTING_SEEDNOISE: {
      //channel1 --> _channelA: from state
      //channel2 --> _channelB: to state
      //channel3 --> _channelC: steptime
      //channel4 --> _channelD: steptime-factor
      //channel5 --> _channelE: seed

      _channelA = channel1;
      _channelB = channel2;
      _channelC = channel3;
      _channelD = channel4;
      _channelE = channel5;

      _state = _channelA->get_state();
      _state1 = _state;
      _state2 = _channelB->get_state();
      _setA = _channelC->get_state(); //steptime
      _setB = _channelD->get_state(); //steptime-factor
      _setC = _channelE->get_state(); //seed

      if(_setB == 0){
        _setB = 1;
      }
      
      _steptime = (unsigned int) _setA * _setB;
      if(_steptime == 0){
        _steptime = 1;
      }
    } break;

    case SETTING_PERLINNOISE: {
      //channel1 --> _channelA: from state
      //channel2 --> _channelB: to state
      //channel3 --> _channelC: steptime
      //channel4 --> _channelD: steptime-factor

      _channelA = channel1;
      _channelB = channel2;
      _channelC = channel3;
      _channelD = channel4;

      _state = _channelA->get_state();
      _state1 = _state;
      _state2 = _channelB->get_state();
      _setA = _channelC->get_state(); //steptime
      _setB = _channelD->get_state(); //steptime-factor

      // The PERLIN_NOISE array has a nice centered value at index 19. Good place to start.
      _intervalstep = 19;

      if(_setB == 0){
        _setB = 1;
      }

      _steptime = (unsigned int) _setA * _setB;
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
          _update_sinwave_inputs(now);
        } break;
        case SETTING_LINEARWAVE: {
          _update_linear_inputs(now);
        } break;
        case SETTING_LINEARSAW: {
          _update_linear_inputs(now);
        } break;
        case SETTING_BEZIERWAVE: {
          _update_bezier_inputs(now);
        } break;
        case SETTING_BEZIERSAW: {
          _update_bezier_inputs(now);
        } break;
        case SETTING_SQUAREWAVE: {
          _update_squarewave_inputs(now);
        } break;
        case SETTING_NOISE: {
          _update_noise_inputs(now);
        } break;
        case SETTING_SEEDNOISE: {
          _update_seednoise_inputs(now);
        } break;
        case SETTING_PERLINNOISE: {
          _update_perlinnoise_inputs(now);
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
          _update_singularlinear();
          _set_state_from_newstate();
        } break;

        // case BEZIERAPPEARFLASH: --> use fall through mechanic: https://stackoverflow.com/questions/4704986/switch-statement-using-or
        case SETTING_SINGULARBEZIER: {
          _update_singularbezier();
          _set_state_from_newstate();
        } break;

        case SETTING_SINWAVE: {
          _update_sinwave();
          _set_state_from_newstate();
        } break;

        case SETTING_LINEARWAVE: {
          _update_linearwave();
          _set_state_from_newstate();
        } break;

        case SETTING_LINEARSAW: {
          _update_linearsaw();
          _set_state_from_newstate();
        } break;

        case SETTING_BEZIERWAVE: {
          _update_bezierwave();
          _set_state_from_newstate();
        } break;

        case SETTING_BEZIERSAW: {
          _update_beziersaw();
          _set_state_from_newstate();
        } break;

        case SETTING_SQUAREWAVE: {
          _update_squarewave();
          _set_state_from_newstate();
        } break;

        case SETTING_NOISE: {
          _update_noise();
          _set_state_from_newstate();
        } break;

        case SETTING_SEEDNOISE: {
          _update_seednoise();
          _set_state_from_newstate();
        } break;

        case SETTING_PERLINNOISE: {
          _update_perlinnoise();
          _set_state_from_newstate();
        } break;
      }
      return _state;
    }
  }
}

void Setting::_update_singularlinear()
{
  // If it is getting brighter
  if(rising()){
            
    _newstate = (int)_state + _steps;
            
    if(_newstate >= _state2 || _newstate > 100){
      _newstate = _state2;
      _type = SETTING_STATIC;
    }
  // If it is getting dimmer
  } else {
            
    _newstate = (int)_state - _steps;
            
    if (_newstate <= _state2 || _newstate < 0){
      _newstate = _state2;
      _type = SETTING_STATIC;
    }
  }
}

void Setting::_update_singularbezier()
{
  //  Bezier Dimming & Direct to Bezier
  _intervalstep = _intervalstep + _steps;
          
  if(rising()){
            
    if(_intervalstep >= _intervalsteps){
      _newstate = _state2;
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
      _newstate = (int) _state1 + _bz * (_state2 - _state1);
    }  
  } else {
            
    if (_intervalstep >= _intervalsteps){
      _newstate = _state2;
      _type = SETTING_STATIC;
    } else {
      _bz = bezier(_intervalstep);
      _newstate = (int) _state1 - _bz * (_state1 - _state2);
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

void Setting::_update_sinwave_inputs(unsigned long now)
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
  if(_intervalsteps == 0){
    _intervalsteps = 1;
  }
}

void Setting::_update_sinwave()
{
  _i = _i + (float) (M_PI / _intervalsteps) * _steps;
  _y = _state1 + ((sin(_i) + 1)/2) * (_state2-_state1);
  _newstate = (int) _y;
}

void Setting::_init_linear_inputs(Channel* channel1, Channel* channel2, Channel* channel3)
{
  //channel1 --> _channelA: from state
  //channel2 --> _channelB: to state
  //channel3 --> _channelC: steptime
  _channelA = channel1;
  _channelB = channel2;
  _channelC = channel3;
  _state = _channelA->get_state();
  _state1 = _state;
  _state2 = _channelB->get_state();
  _steptime = _channelC->get_state();
  if(_steptime == 0){
    _steptime = 1;
  }
}

void Setting::_update_linear_inputs(unsigned long now)
{
  //_channelA: from state
  //_channelB: to state
  //_channelC: steptime
  _state1 = _channelA->get_state(now);
  _state2 = _channelB->get_state(now);
  _steptime = _channelC->get_state(now);
  if(_steptime == 0){
    _steptime = 1;
  }
}

void Setting::_update_linearwave()
{
  // If it is getting brighter
  if(rising()){

    _newstate = (int) _state + _steps;
            
    if(_newstate >= _state2 || _newstate > 100){
      _newstate = _state2;
      // Peak is reached. Flip state inputs.
      _channelD = _channelA;
      _channelA = _channelB;
      _channelB = _channelD;
    }
  // If it is getting dimmer
  } else {
            
    _newstate = (int) _state - _steps;
            
    if (_newstate <= _state2 || _newstate < 0){
      _newstate = _state2;
      // Low is reached. Flip state inputs.
      _channelD = _channelA;
      _channelA = _channelB;
      _channelB = _channelD;
    }
  }
}

void Setting::_update_linearsaw()
{
  if(_reset){
    _newstate = _state1;
    _reset = false;
  } else if(rising()){
    // If it is getting brighter
    _newstate = (int) _state + _steps;
            
    if(_newstate >= _state2 || _newstate > 100){
      _newstate = _state2;
      _reset = true;
    }
  } else {
    // If it is getting dimmer
    _newstate = (int) _state - _steps;
            
    if (_newstate <= _state2 || _newstate < 0){
      _newstate = _state2;
      _reset = true;
    }
  }
}

void Setting::_init_bezier_inputs(Channel* channel1, Channel* channel2, Channel* channel3, Channel* channel4, Channel* channel5, Channel* channel6)
{
  //channel1 --> _channelA: from state
  //channel2 --> _channelB: to state
  //channel3 --> _channelC: steptime
  //channel4 --> _channelD: decisteps
  //channel5 --> _channelE: y1
  //channel6 --> _channelF: y2
  _channelA = channel1;
  _channelB = channel2;
  _channelC = channel3;
  _channelD = channel4;
  _channelE = channel5;
  _channelF = channel6;
  _state = _channelA->get_state();
  _state1 = _state;
  _state2 = _channelB->get_state();
  _steptime = _channelC->get_state();
  _intervalsteps = (unsigned int) _channelD->get_state() * 10; // decisteps per interval. decisteps per change from _state1 to _state2. decisteps per PI.
  _setA = _channelE->get_state();
  _setB = _channelF->get_state();
  if(_steptime == 0){
    _steptime = 1;
  }
  if(_intervalsteps == 0){
    _intervalsteps = 1;
  }
}

void Setting::_update_bezier_inputs(unsigned long now)
{
  //_channelA: from state
  //_channelB: to state
  //_channelC: steptime
  //_channelD: decisteps
  //_channelE: y1
  //_channelF: y2
  _state1 = _channelA->get_state(now);
  _state2 = _channelB->get_state(now);
  _steptime = _channelC->get_state(now);
  _intervalsteps = (unsigned int) _channelD->get_state(now) * 10; // decisteps per interval. decisteps per change from _state1 to _state2.
  _setA = _channelE->get_state(now);
  _setB = _channelF->get_state(now);
  if(_steptime == 0){
    _steptime = 1;
  }
  if(_intervalsteps == 0){
    _intervalsteps = 1;
  }
}

void Setting::_update_bezierwave()
{

  _intervalstep = _intervalstep + _steps;

  if(rising()){
              
    if(_intervalstep >= _intervalsteps){
      _newstate = _state2;
      _intervalstep = 0;
      // High is reached. Flip state inputs.
      _channelG = _channelA;
      _channelA = _channelB;
      _channelB = _channelG;
      // Also flip y1 & y2
      _channelG = _channelE;
      _channelE = _channelF;
      _channelF = _channelG;
    } else {
      _bz = bezier(_intervalstep);
      _newstate = (int) _state1 + _bz * (_state2 - _state1);
    } 
  } else {
              
    if (_intervalstep >= _intervalsteps){
      _newstate = _state2;
      _intervalstep = 0;
      // Low is reached. Flip state inputs.
      _channelG = _channelA;
      _channelA = _channelB;
      _channelB = _channelG;
      // Also flip y1 & y2
      _channelG = _channelE;
      _channelE = _channelF;
      _channelF = _channelG;
    } else {
      _bz = bezier(_intervalstep);
      _newstate = (int) _state1 - _bz * (_state1 - _state2);
    }
  }
}

void Setting::_update_beziersaw()
{

  if(_reset){
    _newstate = _state1;
    _intervalstep = 0;
    _reset = false;
  } else {

    _intervalstep = _intervalstep + _steps;

    if(rising()){
              
      if(_intervalstep >= _intervalsteps){
        _newstate = _state2;
        _reset = true;
      } else {
        _bz = bezier(_intervalstep);
        _newstate = (int) _state1 + _bz * (_state2 - _state1);
      }  
    } else {
              
      if (_intervalstep >= _intervalsteps){
        _newstate = _state2;
        _reset = true;
      } else {
        _bz = bezier(_intervalstep);
        _newstate = (int) _state1 - _bz * (_state1 - _state2);
      }
    }
  }
}


void Setting::_update_squarewave_inputs(unsigned long now)
{
  //_channelA: from state
  //_channelB: to state
  //_channelC: from steptime
  //_channelD: to steptime
  //_channelE: from steptime-factor
  //_channelF: to steptime-factor
  _state1 = _channelA->get_state(now);
  _state2 = _channelB->get_state(now);
  _setA = _channelC->get_state(now); //from steptime
  _setB = _channelD->get_state(now); //to steptime
  _setC = _channelE->get_state(now); //from steptime-factor
  _setD = _channelF->get_state(now); //to steptime-factor

  // steptime-factors are set to 1 if 0
  if(_setC == 0){
    _setC = 1;
  }
  if(_setD == 0){
    _setD = 1;
  }

  // If reset is true we are currentlz at the to state
  if(_reset){
    _steptime = (unsigned int) _setB * _setD;
  } else {
    _steptime = (unsigned int) _setA * _setC;
  }
  if(_steptime == 0){
    _steptime = 1;
  }
}


void Setting::_update_squarewave()
{
  if(_reset){
    _newstate = _state1;
    _reset = false;
  } else {
    _newstate = _state2;
    _reset = true;
  }
}


void Setting::_update_noise_inputs(unsigned long now)
{
  //_channelA: from state
  //_channelB: to state
  //_channelC: steptime
  //_channelD: steptime-factor

  _state1 = _channelA->get_state(now);
  _state2 = _channelB->get_state(now);
  _setA = _channelC->get_state(now); //steptime
  _setB = _channelD->get_state(now); //steptime-factor

  // The random function returns unexpected results if min > max.
  if(_state1 > _state2){
    _setD = _state1;
    _state1 = _state2;
    _state2 = _setD;
  }

  if(_setB == 0){
    _setB = 1;
  }

  _steptime = (unsigned int) _setA * _setB;
  if(_steptime == 0){
    _steptime = 1;
  }
}


void Setting::_update_noise()
{
  randomSeed(micros());
  _newstate = (int) random(_state1, _state2+1);
}


void Setting::_update_seednoise_inputs(unsigned long now)
{
  //_channelA: from state
  //_channelB: to state
  //_channelC: steptime
  //_channelD: steptime-factor
  //_channelE: seed


  _state1 = _channelA->get_state(now);
  _state2 = _channelB->get_state(now);
  _setA = _channelC->get_state(now); //steptime
  _setB = _channelD->get_state(now); //steptime-factor
  _setC = _channelE->get_state(now); //seed

  // The random function returns unexpected results if min > max.
  if(_state1 > _state2){
    _setD = _state1;
    _state1 = _state2;
    _state2 = _setD;
  }

  // If steptime-factor is set to 0, it is set to 1
  if(_setB == 0){
    _setB = 1;
  }

  _steptime = (unsigned int) _setA * _setB;
  if(_steptime == 0){
    _steptime = 1;
  }
}


void Setting::_update_seednoise()
{
  randomSeed(_setC);
  _newstate = (int) random(_state1, _state2+1);
}


void Setting::_update_perlinnoise_inputs(unsigned long now)
{
  //_channelA: from state
  //_channelB: to state
  //_channelC: steptime
  //_channelD: steptime-factor

  _state1 = _channelA->get_state(now);
  _state2 = _channelB->get_state(now);
  _setA = _channelC->get_state(now); //steptime
  _setB = _channelD->get_state(now); //steptime-factor

  if(_setB == 0){
    _setB = 1;
  }

  _steptime = (unsigned int) _setA * _setB;
  if(_steptime == 0){
    _steptime = 1;
  }
}


void Setting::_update_perlinnoise()
{
  _newstate = (int) (_state1 + ((float) pgm_read_float(&PERLIN_NOISE[_intervalstep])) * (_state2 - _state1));
  _intervalstep += 1;
  if(_intervalstep >= PERLIN_SIZE){
    _intervalstep = 0;
  }
}


void Setting::_set_state_from_newstate()
{
  if(_newstate < 0){
    _state = 0;
  }
  else if(_newstate > 100){
    _state = 100;
  }
  else{
    _state = lowByte(_newstate);
  }
}
    
bool Setting::rising()
{
  return (_state < _state2);
}

byte Setting::get_type()
{
  return _type;
}
