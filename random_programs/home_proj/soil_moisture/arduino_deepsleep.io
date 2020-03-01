
#include <ESP8266WiFi.h>
#include <ESPDailyTask.h>
#include <ESP8266HTTPClient.h>


// Replace with your SSID and Password
const char* ssid     = "R-VMVMVM";
const char* password = "somepassword";
ESPDailyTask dailyTask(8*60); // 8 AM 


int pind2 = 4;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  dailyTask.sleep1Day();
  pinMode(2, OUTPUT);
  digitalWrite(2, HIGH); // For some reason HIGH turns off LED  
  pinMode(4, OUTPUT);
  digitalWrite(4, HIGH);
  initWifi();
  analogreadserial();
  pinMode(4, LOW);
  //ESP.deepSleep(30e6);
  // and back to sleep once daily code is done  
  dailyTask.backToSleep();

}

void loop() {
  // put your main code here, to run repeatedly:

}

void initWifi() {
  Serial.print("Connecting to: "); 
  Serial.print(ssid);
  WiFi.begin(ssid, password);  

  int timeout = 10 * 4; // 10 seconds
  while(WiFi.status() != WL_CONNECTED  && (timeout-- > 0)) {
    delay(250);
    Serial.print(".");
  }
  Serial.println("");

  if(WiFi.status() != WL_CONNECTED) {
     Serial.println("Failed to connect, going back to sleep");
     initWifi();
  }

  Serial.print("WiFi connected in: "); 
  Serial.print(millis());
  Serial.print(", IP address: "); 
  Serial.println(WiFi.localIP());
}


void analogreadserial() {
  int sensorValue = analogRead(A0); 
  String va = String(sensorValue);
  // print out the value you read:
  Serial.println(sensorValue);
  if (WiFi.status() == WL_CONNECTED) 
  { //Check WiFi connection status
    HTTPClient Post;
    Post.begin("http://192.168.0.151:5000/moisture"); 
    Post.addHeader("operator", "text/plain");  
    Post.POST("{'moisture_value_basil':  "+ va + "}");
    String payload = Post.getString();
    Serial.println(payload);
    Post.end();
  } 
  delay(500);    
}
