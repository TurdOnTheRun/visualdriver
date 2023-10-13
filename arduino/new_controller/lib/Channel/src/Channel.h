/*
  Channel.h
  Created by Maximilian Weber, April 29, 2023.
*/
#ifndef Channel_h
#define Channel_h

#include "Arduino.h"

class Setting;
class Effect;

static const byte EFFECTSPERCHANNEL = 3;

class Channel {
  private:
    Setting* _setting = nullptr;
    Channel* _channel = nullptr;
    Effect* _effects[EFFECTSPERCHANNEL] = {};
    byte _isstatic = false;
    byte _staticstate = 0;
  
  protected:
    byte _newstate;

  public:
    Channel();
    Channel(byte staticstate);
    Channel(Setting* setting, Channel* channel);
    void init();
    byte get_state(unsigned long now, byte lightid);
    void set_setting(Setting* setting);
    void set_channel(Channel* channel);
    void set_static(byte state);
    void add_effect(Effect* effect, byte index);
    void remove_effect(byte index);
    void remove_effects();
};

#endif
