/*
  Light.cpp - Library for controlling Light.
  Created by Maximilian Weber, Dezember 25, 2020.
*/

#include "Arduino.h"
#include "Light.h"

Light::Light(byte id, byte pin)
{
  _pin = pin;
  _id = id;
}

void Light::init()
{
  pinMode(_pin, OUTPUT);
}

void Light::setstate(byte newstate)
{
  analogWrite(_pin, newstate);
  _state = newstate;
  _laststep = millis();
}

void Light::update()
{
  if(changing()){
    
    unsigned long passed = millis() - _laststep;

    if (passed < _steptime){
      return;
    }

    switch(_type) {
  
      case 1: {
        //  Linear Dimming & Direct to Linear
        int steps = (int) round(passed/_steptime);
    
        int newstate;
        
        if(rising()){
          
          newstate = ((int)_state) + steps;
          
          if(newstate >= _tostate || newstate > 255){
            setstate(_tostate);
            // For Lighning Appear (6)
            if(_set1 > 0){
              _steptime = _set1;
              _tostate = 0;
              _type = 4;
            }
          } else {
            setstate(lowByte(newstate));
          }
          
        } else {
          
          newstate = ((int)_state) - steps;
          
          if (newstate <= _tostate || newstate < 0){
            setstate(_tostate);
          } else {
            setstate(lowByte(newstate));
          }
          
        }
      } break;

      case 2: {
        //  Strobe
        if(_state == 0){
          setstate(_tostate);
          _tostate = 0;
        } else {
          _tostate = _state;
          setstate(0);
        }
      } break;

      case 4: {
        // Lightning
        setstate(_tostate);
      } break;

      case 5: {
        // Lightning Disappear
        _steptime = _set1;
        // Set to 0 so it doesn't catch in linear as a Lighning Appear
        _set1 = 0;
        _type = 1;
        _laststep = millis();
      } break;

      case 6: {
        // Lighning Appear
        // Needs no code
      } break;

      case 7: {
        // Machine Gun
        if(_state == 0){
          setstate(_tostate);
          _tostate = 0;
          _set1 = _set1 - 1;
        } else {
          _tostate = _state;
          setstate(0);
          if(_set1 == 0){
            _tostate = 0;
          }
        }
      } break;

      case 8: {
        // Accelerating Lightning
        if(_state == 0){
          setstate(_tostate);
          // If there will be a next darkstep
          // If not it'll stay on 
          if(_set1 != 0){
            _tostate = 0;
            _steptime = _set3;
          }
        } else {
          _tostate = _state;
          setstate(0);
          _set3 = _steptime;
          _steptime = _set1;
          if(_set1 > _set2){
            _set1 = _set1 - _set2;
          } else {
            // Set to 0 if reaching <=0 with next subtraction
            _set1 = 0;
          }
        }
      } break;

    }
  }
}

void Light::setto(byte type, byte state1, byte state2, byte steptime, byte set1, byte set2, byte set3)
{
  if(type == 0){
    // Direct_steps
    setstate(state1);
    _tostate = state1;
  }
  else if(type == 1){
    // Linear
    if(steptime == 0){
      setstate(state1);
      _tostate = state1;
    } else {
      _steptime = steptime;
      _tostate = state1;
      _laststep = millis();
    }
    _set1 = 0;
  }
  else if(type == 2){
    // Strobe
    if(_state == state1){
      setstate(0);
      _tostate = state1;
    } else {
      setstate(state1);
      _tostate = 0;
    }
    _steptime = steptime;
  }
  else if(type == 3){
    // Direct to Linear
    if(steptime == 0){
      setstate(state2);
      _tostate = state2;
    } else {
      setstate(state1);
      _steptime = steptime;
      _tostate = state2;
      _laststep = millis();
    }
    type = 1;
  }
  else if(type == 4){
    // Lightning
    setstate(state1);
    _steptime = steptime;
    _tostate = 0;
  }
  else if(type == 5){
    // Lightning Disappear
    setstate(state1);
    // milliseconds on
    _steptime = set1;
    _set1 = steptime;
    _tostate = state2;
  }
  else if(type == 6){
    // Lighning Appear
    setstate(state1);
    _steptime = steptime;
    // milliseconds on
    _set1 = set1;
    _tostate = state2;
    type = 1;
  }
  else if(type == 7){
    // Machine Gun
    if(_state == state1){
      setstate(0);
      _tostate = state1;
      _set1 = state2;
    } else {
      setstate(state1);
      _tostate = 0;
      _set1 = state2 - 1;
    }
    _steptime = steptime;
  }
  else if(type == 8){
    // Accelerating Strobe
    setstate(state1);
    _tostate = 0;
    // steptime is lighttime
    _steptime = steptime;
    // darktime start
    _set1 = set1;
    // darktime decrease
    _set2 = set2;
  }
  _type = type;
}

bool Light::changing()
{
  return !(_state == _tostate);
}
    
bool Light::rising()
{
  return (_state < _tostate);
}

byte Light::getid()
{
  return _id;
}
