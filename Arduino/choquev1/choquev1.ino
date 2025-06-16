void setup() {
  pinMode(8, OUTPUT);
  digitalWrite(8, HIGH); 
  Serial.begin(9600);
}

void loop() {
  int safety = 0;
  digitalWrite(8, HIGH);
  if (Serial.available()) {
    char c = Serial.read();
    if (c == 's') {
      digitalWrite(8, LOW);
      delay(500);
      digitalWrite(8, HIGH);
      delay(1000);
      safety++;
    } 
  }
}
