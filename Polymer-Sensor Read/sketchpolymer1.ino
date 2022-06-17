#define LED_pin 10
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(LED_pin, OUTPUT);
pinMode(7,OUTPUT);

}


void loop() {
  digitalWrite(7,1);
  int Sensor_value = analogRead(A1);
  Serial.println(analogRead(A1));
  if(Sensor_value> 500)
  {
    analogWrite(10,LOW);
  }
  else
  {
    analogWrite(10,HIGH);
  }
  digitalWrite(7,0);
  delay(100);
}
