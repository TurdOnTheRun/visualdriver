/* WiFi server that forwards to Serial through existing access point */
#include <ESP8266WiFi.h>
#include <ArduinoWiFiServer.h>

#ifndef STASSID
#define STASSID "______________"
#define STAPSK "kerze123!"
#endif

const char* ssid = STASSID;
const char* password = STAPSK;

ArduinoWiFiServer server(2323);

void setup() {

  Serial.begin(115200);

  // Serial.println();
  // Serial.print("Connecting to ");
  // Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    // Serial.print(".");
  }

  server.begin();

  // IPAddress ip = WiFi.localIP();
  // Serial.println();
  // Serial.println("Connected to WiFi network.");
  // Serial.print("To access the server, connect with Telnet client to ");
  // Serial.print(ip);
  // Serial.println(" 2323");
}

void loop() {
  WiFiClient client = server.available();     // returns first client which has data to read or a 'false' client
  if (client) {                               // client is true only if it is connected and has data to read
    while(client.connected()){
      if(client.available()){
        Serial.write(client.read());                        // print the message to Serial Monitor
      }
      client.stop();
    }
  }
}
