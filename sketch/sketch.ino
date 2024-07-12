void setup(){
    // Inicializa a comunicação serial com o PC e o módulo Bluetooth
    Serial.begin(9600)
    Serial1.begin(9600)     
}

void loop(){
    // transmite os dados do monitor serial para o bluetooth
    if(Serial.available())  {
        char c = Serial.read();
        Serial1.write(c);    
    }

    // transmite os dados do bluetooth para o monitor serial 
    if(Serial1.available())  {
        char c = Serial1.read();
        Serial.write(c);    
    }
    
}
