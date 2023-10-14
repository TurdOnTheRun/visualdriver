/*
  Setting.h - Library for controlling Setting.
  Created by Maximilian Weber, April 2, 2023.

  Types:
  1 - 9 - Static Types
  10-19 - Linear Types
  20-29 - Bezier Types
*/
#ifndef Setting_h
#define Setting_h

#include "Arduino.h"
class Channel;

class Setting {
  private:
    byte _type=0;
    Channel* _channelA=nullptr;
    Channel* _channelB=nullptr;
    Channel* _channelC=nullptr;
    Channel* _channelD=nullptr;
    Channel* _channelE=nullptr;
    Channel* _channelF=nullptr;
    Channel* _channelG=nullptr;

    byte _state=0;
    byte _state1=0;
    byte _state2=0;
    unsigned int _steptime=0;
    unsigned int _steps=0;
    unsigned long _laststep = 0;
    byte _setA=0;
    byte _setB=0;
    byte _setC=0;
    byte _setD=0;

    // General
    int _newstate=0;
    void _set_state_from_newstate();
    // _intervalsteps is used by SINGULARBEZIER, SIN,
    // One interval is one change from _state1 to _state.
    // For example for SIN this is equal to PI
    unsigned int _intervalsteps=0;
    unsigned int _intervalstep=0;
    // _reset is used by saw waves and square waves.
    // Square waves use the boolean to keep track of to or from
    bool _reset = false;


    // Init & Update Functions
    void _update_singularlinear();
    void _update_singularbezier();

    void _update_sinwave_inputs(unsigned long now);
    void _update_sinwave();

    void _init_linear_inputs(Channel* channel1, Channel* channel2, Channel* channel3);
    void _update_linear_inputs(unsigned long now);
    void _update_linearwave();
    void _update_linearsaw();

    void _init_bezier_inputs(Channel* channel1, Channel* channel2, Channel* channel3, Channel* channel4, Channel* channel5, Channel* channel6);
    void _update_bezier_inputs(unsigned long now);
    void _update_bezierwave();
    void _update_beziersaw();

    void _update_squarewave_inputs(unsigned long now);
    void _update_squarewave();


    // Bezier
    float lerp(float n1, float n2, float perc);
    float bezier(unsigned int step);

    float _bz=0;

    float _i=0;

    float _ya=0;
    float _yb=0;
    float _yc=0;

    float _ym=0;
    float _yn=0;

    float _diff=0;

    float _y=0;
    
  public:
    Setting();
    Setting(byte type, byte set1, byte set2, byte set3, byte set4, byte set5, byte set6);
    Setting(byte type, Channel* channel1, Channel* channel2, Channel* channel3, Channel* channel4, Channel* channel5, Channel* channel6);
    byte get_state();
    byte get_state(unsigned long now);
    byte get_type();
    bool rising();
};

#endif
