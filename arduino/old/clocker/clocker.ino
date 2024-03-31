#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_GFX.h>

#define OLED_WIDTH 128
#define OLED_HEIGHT 64
#define OLED_ADDR   0x3C
Adafruit_SSD1306 display(OLED_WIDTH, OLED_HEIGHT);

byte rtcPin = 2;
byte topPin = 19;
byte bottomPin = 18;

// variables and functions for time keeping
unsigned long now = 0;
unsigned int fract = 0;
void rtc_millis_routine();

// variables and functions for syncing
unsigned long interval1 = 0;
unsigned long interval2 = 0;
bool interval1State = false;
bool interval2State = false;
void sync_interval1_routine();
void sync_interval2_routine();

int delta = 999999;
int lastDelta = 0;

void setup() {
  // Display Setup
  display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDR);
  display.clearDisplay();
  display.display();

  // Interrupts Setup
  attachInterrupt(digitalPinToInterrupt(rtcPin), rtc_millis_routine, FALLING);
  pinMode(topPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(topPin), sync_interval1_routine, CHANGE);
  pinMode(bottomPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(bottomPin), sync_interval2_routine, CHANGE);
}

void loop() {
  if(interval1State == interval2State){
    delta = interval1 - interval2;
    if(delta != lastDelta){
      display.clearDisplay();
      display.setTextSize(4);
      display.setTextColor(WHITE);
      display.setCursor(20, 30);
      display.println(delta);
      display.display();
      lastDelta = delta;
    }
  }
}

void rtc_millis_routine() {
  now += 1;
  fract += 3;
  if(fract >= 125){
    now -= 1;
    fract -= 125;
  }
}

void sync_interval1_routine(){
  interval1 = now;
  interval1State = !interval1State;
}

void sync_interval2_routine(){
  interval2 = now;
  interval2State = !interval2State;
}
