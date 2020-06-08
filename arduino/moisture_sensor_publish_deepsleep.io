

#define uS_TO_S_FACTOR 1000000  /* Conversion factor for micro seconds to seconds */
#define TIME_TO_SLEEP  1800
/* Time ESP32 will go to sleep (in seconds) */
#include <WiFiMulti.h>
#include <HTTPClient.h>
#include <iostream>  
#include<sstream>  

const char* serverName = "http://192.168.0.151:5000/moisture";

WiFiMulti WiFiMulti;

RTC_DATA_ATTR int bootCount = 0;
const int moistPin = 34;
const int moistPwr = 18;

int moistValue = 0;


void print_wakeup_reason(){
  esp_sleep_wakeup_cause_t wakeup_reason;

  wakeup_reason = esp_sleep_get_wakeup_cause();

  switch(wakeup_reason)
  {
    case ESP_SLEEP_WAKEUP_EXT0 : Serial.println("Wakeup caused by external signal using RTC_IO"); break;
    case ESP_SLEEP_WAKEUP_EXT1 : Serial.println("Wakeup caused by external signal using RTC_CNTL"); break;
    case ESP_SLEEP_WAKEUP_TIMER : Serial.println("Wakeup caused by timer"); break;
    case ESP_SLEEP_WAKEUP_TOUCHPAD : Serial.println("Wakeup caused by touchpad"); break;
    case ESP_SLEEP_WAKEUP_ULP : Serial.println("Wakeup caused by ULP program"); break;
    default : Serial.printf("Wakeup was not caused by deep sleep: %d\n",wakeup_reason); break;
  }
}



void wificonnect(){
    Serial.begin(115200);
    delay(10);

    // We start by connecting to a WiFi network
    WiFiMulti.addAP("xxxx", "xxxx");

    Serial.println();
    Serial.println();
    Serial.print("Waiting for WiFi... ");

    while(WiFiMulti.run() != WL_CONNECTED) {
        Serial.print(".");
        delay(2000);
    }

    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());

    delay(500);
}

void moistVal(){
  delay(2000);
  moistValue = analogRead(moistPin);
  Serial.println(moistValue);
  delay(1000);
  if(WiFi.status()== WL_CONNECTED){
    HTTPClient http;
  http.begin(serverName);
  // we send this byte string to docker server and it publishes it further.
  http.addHeader("Content-Type", "text/plain");
  int httpResponseCode = http.POST("{ 'raised_bed_1': "+String(moistValue)+"}");// This took a lot of time as wel
  Serial.print("HTTP Response code: ");
  Serial.println(httpResponseCode);
  http.end();
  }
}


void setup(){
  Serial.begin(115200);
  delay(1000); //Take some time to open up the Serial Monitor

  //Increment boot number and print it every reboot
  ++bootCount;
  Serial.println("Boot number: " + String(bootCount));  

  //Print the wakeup reason for ESP32
  print_wakeup_reason();
  pinMode(moistPwr, OUTPUT); // This took a lot of time! 
  digitalWrite(moistPwr, HIGH);
  wificonnect();
  moistVal();
  digitalWrite(moistPwr, LOW);
  /*
  First we configure the wake up source
  We set our ESP32 to wake up every 5 seconds
  */
  esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR);
  Serial.println("Setup ESP32 to sleep for every " + String(TIME_TO_SLEEP) +
  " Seconds");


  Serial.println("Going to sleep now");
  delay(1000);
  Serial.flush();
  esp_deep_sleep_start();
  Serial.println("This will never be printed");
}

void loop(){

  //This is not going to be called
}
