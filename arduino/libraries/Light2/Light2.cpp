/*
  Light.cpp - Library for controlling Light.
  Created by Maximilian Weber, Dezember 25, 2020.
*/

// #include "Arduino.h"
#include "Light.h"
#include <math.h>

Light::Light(byte id, byte pin)
{
  _pin = pin;
  _id = id;
}

void Light::init()
{
  pinMode(_pin, OUTPUT);
}

void Light::setpinstate(byte newstate)
{
  if(newstate > 100){
    newstate = 100;
  }
  if(_pinstate != newstate){
    analogWrite(_pin, _statemap[newstate]);
    _pinstate = newstate;
  }
}

void Light::update()
{
  // state = setting.get_state(_id)
  // for effect in effects:
  //    state = effect.get_state(state, _id)
  // setpinstate(state);
}





// This goes to the setting
void Light::setstate(byte newstate)
{
  if(newstate > 100){
    newstate = 100;
  }
  _state = newstate;
  _laststep = millis();
}

void Light::update()
{

  _now = millis();

  if(changing()){
    
    _passed = _now - _laststep;

    if (_passed >= _steptime){

      switch(_type) {
    
        case 1: {
          //  Linear Dimming & Direct to Linear
          int steps = (int) round(_passed/_steptime);
      
          int newstate;
          
          if(rising()){
            
            newstate = ((int)_state) + steps;
            
            if(newstate >= _tostate || newstate > 100){
              setstate(_tostate);
              // For Lightning Appear (6)
              // Set how long light should stay at _tostate
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

        case 10: {
          //  Bezier Dimming & Direct to Bezier
          int steps = (int) round(_passed/_steptime);

          if(steps == 0){
            break;
          }
      
          _bezierstep = _bezierstep + steps;
          
          if(rising()){
            
            if(_bezierstep >= 100){
              setstate(_tostate);
              if(_set5 > 0){
                _steptime = _set5;
                _tostate = 0;
                _type = 4;
              }
            } else {
              int newstate;
              float bz = bezier(_bezierstep);
              newstate = (int) round(_fromstate + bz * (_tostate - _fromstate));
              setstate(lowByte(newstate));
            }
            
          } else {
            
            if (_bezierstep >= 100){
              setstate(_tostate);
            } else {
              int newstate;
              float bz = bezier(_bezierstep);
              newstate = (int) round(_fromstate - bz * (_fromstate - _tostate));
              setstate(lowByte(newstate));
            }
          }
        } break;

        case 11: {
          // Lightning Bezier Disappear
          _steptime = _set5;
          // Set to 0 so it doesn't catch in linear as a Lighning Appear
          _set5 = 0;
          _type = 10;
          _laststep = millis();
        } break;
      }
    }
  }
  if(_hasvibrato==true){

    _passed = _now - _vibratolaststep;
    if (_passed >= _vibratosteptime){
      _vibratoangle = _vibratoangle + _vibratostepangle * _passed/_vibratosteptime;
      // if(_vibratoangle > 2 * M_PI){
      //   _vibratoangle = _vibratoangle - (2 * M_PI);
      // }
      int vibratostate;
      switch(_vibratotype) {
        case 1: {
          vibratostate = (int) round(_state + _state * _updownvibrato(_vibratoangle) * _vibratoamplitude);
        } break;
        case 2: {
          vibratostate = (int) round(_state + _state * _upvibrato(_vibratoangle) * _vibratoamplitude);
        } break;
        default: {
          vibratostate = (int) round(_state + _state * _downvibrato(_vibratoangle) * _vibratoamplitude);
        } break;
      }
      if(vibratostate > 100){
        vibratostate = 100;
      } else if(vibratostate < 0){
        vibratostate = 0;
      }
      // Serial.println(_vibratoangle);
      // Serial.println(vibratostate);
      // Serial.println();
      setpinstate(lowByte(vibratostate));
      _vibratolaststep = millis();
    }

  } else if (_state != _pinstate){
    setpinstate(_state);
  }

}

void Light::setto(byte type, byte state1, byte state2, byte steptime, byte set1, byte set2, byte set3, byte set4, byte set5)
{
  if(type == 0){
    // Direct_steps
    setstate(state1);
    _tostate = state1;
    _type = type;
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
    _type = type;
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
    _type = type;
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
    _type = type;
  }
  else if(type == 4){
    // Lightning
    setstate(state1);
    _steptime = steptime;
    _tostate = 0;
    _type = type;
  }
  else if(type == 5){
    // Lightning Disappear
    setstate(state1);
    // milliseconds on
    _steptime = set1;
    // steptime for dimming
    _set1 = steptime;
    // dimm to state
    _tostate = state2;
    _type = type;
  }
  else if(type == 6){
    // Lightning Appear
    setstate(state1);
    // steptime for dimming
    _steptime = steptime;
    // milliseconds on
    _set1 = set1;
    // dimm to state
    _tostate = state2;
    type = 1;
    _type = type;
  }
  else if(type == 7){
    // Machine Gun
    // if the current state = state1, start with off
    if(_state == state1){
      setstate(0);
      _tostate = state1;
      _set1 = state2;
    // else start with state1 and count it as first shot
    } else {
      setstate(state1);
      _tostate = 0;
      _set1 = state2 - 1;
    }
    _steptime = steptime;
    _type = type;
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
    _type = type;
  }
  else if(type == 10){
    // Bezier Dimm
    if(steptime == 0){
      setstate(state2);
      _tostate = state2;
      type = 0;
    } else {
      _steptime = steptime;
      _fromstate = state1;
      _tostate = state2;
      _set1 = set1;
      _set2 = set2;
      _set3 = set3;
      _set4 = set4;
      _bezierstep = 0;
      setstate(state1);
    }
    _type = type;
  }
  else if(type == 11){
    _fromstate = state1;
    _tostate = state2;
    _set1 = set1;
    _set2 = set2;
    _set3 = set3;
    _set4 = set4;
    _bezierstep = 0;
    if(_fromstate < _tostate){
      // Lightning Bezier Appear
      // bezier steptime
      _steptime = steptime;
      // milliseconds on
      _set5 = set5;
      type = 10;
    } else if(_fromstate > _tostate) {
      // Lightning Bezier Disappear
      // milliseconds on
      _steptime = set5;
      // bezier steptime
      _set5 = steptime;
    } else {
      steptime = set5;
      type = 4;
    }
    setstate(state1);
    _type = type;
  }
  else if(type = 12){
    // Vibrato
    // state1 sets vibratotype
    _vibratotype = state1;
    if(_vibratotype == 0){
      _hasvibrato = false;
    } else {
      // state2 sets amplitude percentage
      _vibratoamplitude = (float) state2 / 100;
      _vibratosteptime = steptime;
      _hasvibrato = true;
      _vibratolaststep = millis();
    }
    // Serial.println(_vibratotype);
    // Serial.println(_hasvibrato);
    // Serial.println(_vibratoamplitude);
    // Serial.println(_vibratosteptime);
    // Serial.println();
  }
}

float Light::lerp(float n1, float n2, float perc)
{
  float diff = n2 - n1;
  return n1 + ( diff * perc );
}

float Light::bezier(byte step)
{ 
  // There are a total of 100 steps
  float i = 0.01 * step;

  // The Green Lines
  float xa = lerp( 0 , _set1 , i );
  float ya = lerp( 0 , _set2 , i );
  float xb = lerp( _set1 , _set3 , i );
  float yb = lerp( _set2 , _set4 , i );
  float xc = lerp( _set3 , 100 , i );
  float yc = lerp( _set4 , 100 , i );

  // The Blue Line
  float xm = lerp( xa , xb , i );
  float ym = lerp( ya , yb , i );
  float xn = lerp( xb , xc , i );
  float yn = lerp( yb , yc , i );

  // The Black Dot
  float y = lerp( ym , yn , i ) / 100;
  return y;
}

float Light::_updownvibrato(float angle)
{ 
  return sin(angle);
}

float Light::_upvibrato(float angle)
{ 
  return (cos(angle) * (-1) + 1)/2;
}

float Light::_downvibrato(float angle)
{ 
  return (cos(angle)-1)/2;
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
