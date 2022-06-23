void setup() {
  Serial.begin(9600);
  pinMode(7,OUTPUT);

}

void loop() {
  digitalWrite(7,1);
  Serial.println(analogRead(A1));
  digitalWrite(7,0);
  delay(100);
}
