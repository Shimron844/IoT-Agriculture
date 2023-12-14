int incomingByte = 0;
int led = 13;
int motor = 12;
int sensor_pin = A1;
int proximity_pin = 2;
int proximity_out = 3;
#include <dht.h>        // Include library
#define outPin 8        // Defines pin number to which the sensor is connected

dht DHT;   


void setup() {
Serial.begin(9600);
pinMode(proximity_out, OUTPUT);
pinMode(proximity_pin, INPUT);
pinMode(sensor_pin, INPUT);
pinMode(motor, OUTPUT);
pinMode(led, OUTPUT);
}

void loop() {

if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
    if (incomingByte == 'H') {
      digitalWrite(led, HIGH);
    }
    // if it's an L (ASCII 76) turn off the LED:
    if (incomingByte == 'L') {
      digitalWrite(led, LOW);
    }
  }

  sensor_pin_high();
  int readData = DHT.read11(outPin);

	float t = DHT.temperature;        // Read temperature
	float h = DHT.humidity;  // Read humidity      


	// Serial.print(t);   // Temperature in celsius
	// Serial.print((t*9.0)/5.0+32.0);        // Convert celsius to fahrenheit



  float moisture_percentage;
  int sensor_analog;
  sensor_analog = analogRead(sensor_pin);
  moisture_percentage = ( 100 - ( (sensor_analog/1023.00) * 100 ) );

  Serial.print("\n");
  Serial.print(t);
  Serial.print(",");
  Serial.print(h);
  Serial.print(",");
  Serial.print(moisture_percentage);
  Serial.print("\n");
  delay(500);

}


   void sensor_pin_high() {
    int sensor_value = digitalRead(proximity_pin);

    if(sensor_value == LOW){
      digitalWrite(proximity_out, LOW);
    }else{
      digitalWrite(proximity_out, HIGH);
    }
    }

