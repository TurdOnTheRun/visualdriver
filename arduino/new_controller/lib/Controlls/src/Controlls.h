/*
  Controlls.h - Library for controlling Controlls.
  Created by Maximilian Weber, April 29, 2023.

  Types:
  1 - 9 - Static Types
  10-19 - Linear Types
  20-29 - Bezier Types
*/
#ifndef Controlls_h
#define Controlls_h

#include "Arduino.h"

// 1-50 are settings
static const byte SETTING_STATICLIGHT = 1;
static const byte SETTING_STATICFLASH = 2;
static const byte SETTING_STATICMACHINE = 3;
static const byte SETTING_LINEARDIMM = 10;
static const byte SETTING_BEZIERDIMM = 20;

static const byte EFFECT_UPVIBRATO = 60;
static const byte EFFECT_DOWNVIBRATO = 61;
static const byte EFFECT_UPDOWNVIBRATO = 62;
static const byte EFFECT_STROBE = 70;

static const byte LIGHT_SET_CHANNEL = 150;

static const byte CHANNEL_SET_SETTING = 160;
static const byte CHANNEL_SET_CHANNEL = 161;
static const byte CHANNEL_ADD_EFFECT = 170;
static const byte CHANNEL_REMOVE_EFFECT = 171;
static const byte CHANNEL_REMOVE_EFFECTS = 172;

#endif
