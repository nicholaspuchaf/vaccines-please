void setup() {
  pinMode(8, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int safety = 0;
  if (Serial.available()) {
    char c = Serial.read();
    if (c == 's') {
      digitalWrite(8, HIGH);
      safety++;
    } 
  }
}
