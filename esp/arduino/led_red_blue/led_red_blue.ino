
 
// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int led1 = 2;
int led2 = 8;



// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(led1, OUTPUT); 
  pinMode(led2, OUTPUT);  

}

// the loop routine runs over and over again forever:
void loop() {
  digitalWrite(led1, HIGH);  
  digitalWrite(led2, HIGHwhich );
}
