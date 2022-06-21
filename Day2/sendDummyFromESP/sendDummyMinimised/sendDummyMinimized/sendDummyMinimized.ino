#include <ESP8266WiFi.h>

WiFiClient wifiClient;

void setup(){
 Serial.begin(9600);
 WiFi.begin("RCA-WiFi", "rca@2019");
}


void loop(){
 String mData="device=\"Group-SAUVE-Section2\"&distance=\"697 cm\"";
 sendData(80, "insecure.benax.rw", "/iot/" , mData); 
 delay(5000);
}

void sendData(const int httpPort, const char* host,const char* filepath , String data){
  
  wifiClient.connect(host, httpPort); 

  wifiClient.println("POST "+(String)filepath+" HTTP/1.1");
  wifiClient.println("Host: " + (String)host);
  wifiClient.println("User-Agent: ESP8266/1.0");
  wifiClient.println("Content-Type: application/x-www-form-urlencoded");
  wifiClient.println("Content-Length: " +(String)data.length());
  wifiClient.println();
  wifiClient.print(data);

  Serial.println("Response: " + wifiClient.readStringUntil('\n'));

}