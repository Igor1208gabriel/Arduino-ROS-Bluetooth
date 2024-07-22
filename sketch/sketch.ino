int trigPin = 9;    // TRIG pin
int echoPin = 8;    // ECHO pin

float duration_us, distance_cm;

float calculate_distance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration_us = pulseIn(echoPin, HIGH);
  distance_cm = 0.017 * duration_us;
  return distance_cm;
}

void setup() {
  // Inicializa a comunicação serial com o PC e com o módulo Bluetooth
  Serial.begin(9600);
  Serial1.begin(9600);  // Serial1 é a comunicação serial nos pinos 18 (TX1) e 19 (RX1)
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  float sum = 0;
  int validReadings = 0;

  for (int i = 0; i < 10; i++) {
    float distancia = calculate_distance();
    if (distancia > 0 && distancia <= 150) {
      sum += distancia;
      validReadings++;
    }
  }

  if (validReadings > 0) {
    float media = sum / validReadings;
    char cstr[16];
    dtostrf(media, 6, 2, cstr);  // Converte float para string
    Serial.println(cstr);       // Envia para a Serial para debug
    Serial1.write(cstr);        // Envia para Serial1
    Serial1.write('\n');
  }


  if (Serial.available()) {
    char c = Serial.read();
    Serial1.write(c);
  }

  if (Serial1.available()) {
    char c = Serial1.read();
    Serial.write(c);
   }

  delay(1000);
}