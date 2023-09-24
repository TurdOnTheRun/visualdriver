/*
  Motor.h - Library for controlling Motor via H-Bridge.
  Created by Maximilian Weber, September 24, 2023.
*/
#ifndef Motor_h
#define Motor_h

#include "Arduino.h"
#include "Controlls.h"


class Motor {
  private:
    byte _LPWM_pin;
    byte _RPWM_pin;
    byte _OUT_pin;
    byte _NOTOUT_pin;
    boolean _stopped = true;
    boolean _changingDirection = false;
    byte _pinstate;
    byte _state;
    byte _tostate;
    int _newstate;
    byte _savestate;
    byte _steptime;
    unsigned long _laststep;

  protected:
    void set_pinstate();
    virtual void pin_write();

  public:
    Motor(byte LPWM_pin, byte RPWM_pin);
    void init();
    void set_to(byte state, byte steptime, unsigned long now);
    void update(unsigned long now);
    void changedirection();
    bool changing();
    bool rising();
};

#endif
