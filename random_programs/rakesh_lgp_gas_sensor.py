/* This project is to detect LPG Gas Leak in my home in India. This was requested by mom and this is my first ever Arduino Project */

int redLed = 12;
int buzzer = 10;
int smokeA0 = A5;
int sensorThres = 95;

void setup() {
  pinMode(redLed, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(smokeA0, INPUT);
  Serial.begin(9600);
}

void loop() {
  int analogSensor = analogRead(smokeA0);

  Serial.print("Pin A0: ");
  Serial.println(analogSensor);
  // Checks if it has reached the threshold value
  if (analogSensor > sensorThres)
  {
    digitalWrite(redLed, LOW);
    delay(100);
    digitalWrite(redLed, HIGH);
    delay(100);
    tone(buzzer, 1000, 200);
  }
  else
  {
    digitalWrite(redLed, HIGH);
    noTone(buzzer);
  }
  delay(100);
}
