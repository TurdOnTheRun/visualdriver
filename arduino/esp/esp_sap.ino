/* WiFi access point that forwards to Serial. */

#include <ESP8266WiFi.h>
#include <ArduinoWiFiServer.h>

#ifndef APSSID
#define APSSID "Old Weller"
#define APPSK "wellalright!"
#endif

/* Set these to your desired credentials. */
const char *ssid = APSSID;
const char *password = APPSK;

ArduinoWiFiServer server(2323);

void setup() {
  Serial.begin(115200);
  delay(10);

  // Set up SoftAP
  WiFi.softAP(ssid, password);
  delay(100);
  // IPAddress myIP = WiFi.softAPIP();
  // Serial.print("SoftAP IP address: ");
  // Serial.println(myIP);
  server.begin();
}

void loop() {
  WiFiClient client = server.available();
  if (client) {
    while (client.connected()) {
      if (client.available()) {
        Serial.write(client.read());
      }
    }
    client.stop();
  }
}
