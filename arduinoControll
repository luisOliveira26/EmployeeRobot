// C++ code 
// incluir bibliotecas 
#include <Wire.h>                   
#include <BnrOmni.h> 
#include <Pixy2.h> 
#include "SoftwareSerial.h" 
Pixy2 pixy; 
// definir pinos 
//PINO 0 e 1, utilizados para UART   
#define ULTRASONIC1_TRIG_PIN 6      
// sensor 1  
#define ULTRASONIC1_ECHO_PIN 7     // sensor 1 
#define ULTRASONIC2_TRIG_PIN 3      
// sensor 2 
#define ULTRASONIC2_ECHO_PIN 2      // sensor 2 
#define ULTRASONIC3_TRIG_PIN 5      
// sensor 3 
#define ULTRASONIC3_ECHO_PIN 4      // sensor 3 
int saida8 =8; 
int saida9 =9; 
int saida16 =16; 
int entrada17 =17; 
//PINO 10 ao 13, para SPI   
#define RX_PIN A0 // BT 
#define TX_PIN A1 // BT 
//PINO A4 e A5, para I2C   
#define OMNI3MD_ADDRESS 0x30        
#define M1  1    // Motor1 
#define M2  2    // Motor2 
#define M3  3    // Motor3 
// default factory address 
Luís Oliveira  
Técnico de Mecatrónica – Triénio 2019/2022 
 
IMP.21 – V01 
Página 87 
PAP 
SchoolBot 
String readString; 
//comunicação com a APP 
SoftwareSerial nss( RX_PIN, TX_PIN); 
// dar um nome a cada valor 
typedef enum 
{ 
colorGreen  = 1, 
colorRed    = 2, 
colorBlue   = 3, 
colorYellow = 4, 
colorroxo = 7, 
} pixyColor; 
// dados enviados pela app 
int val[2]; 
// definir o centro do analógico como o inicio 
float valorx = 125; 
float valory = 125; 
BnrOmni omni; //declaration of object variable to control the Omni3MD// 
// criação de algumas variaveis (distancias em cm) 
int distancia30 = 30;    
int distancia40 = 40; 
int distancia50 = 50; 
int distancia55 = 55; 
int distancia60 = 60; 
int distancia70 = 70; 
int distancia80 = 80; 
// variavel que diz que o controlo é feito pela app ou automático 
Luís Oliveira  
Técnico de Mecatrónica – Triénio 2019/2022 
 
IMP.21 – V01 
Página 88 
PAP 
SchoolBot 
int start = 0; 
// criação de outras variaveis 
int distanciaDif = 0; 
int distanciaMin =0; 
float veloz =  0; 
float vel = 0; 
float radpos =  0; 
float angpos =  0; 
float radneg =  0; 
float angneg = 0; 
float velocidade = 0; 
int mov = 2; 
int salaGreen= 1; 
int salaRed = 1; 
int salaBlue = 1; 
int salaYellow = 1; 
int distanciaS3; 
int lastValidValueS1 = 0, lastValidValueS2 = 0; 
// valor lido pelos sensores ultrassons 
void updateUltrasonicDistance(void) 
{ 
int distanciaS1, distanciaS2; 
// sensor 1 
digitalWrite(ULTRASONIC1_TRIG_PIN, LOW); 
delayMicroseconds(2); 
// Sets the trigger pin to HIGH state for 10 microseconds 
digitalWrite(ULTRASONIC1_TRIG_PIN, HIGH); 
delayMicroseconds(10); 
digitalWrite(ULTRASONIC1_TRIG_PIN, LOW); 
Luís Oliveira  
Técnico de Mecatrónica – Triénio 2019/2022 
 
IMP.21 – V01 
Página 89 
 
Luís Oliveira  
Técnico de Mecatrónica – Triénio 2019/2022 
 
IMP.21 – V01 
Página 90 
 
PAP 
SchoolBot 
  
  // Reads the echo pin, and returns the sound wave travel time in microseconds 
 // limpar os valores que forem igual a 0 
  distanciaS1 = pulseIn(ULTRASONIC1_ECHO_PIN, HIGH) * 0.01723;  
  if (distanciaS1 != 0) 
  { 
    lastValidValueS1 = distanciaS1; 
  } 
  // sensor 2  
  digitalWrite(ULTRASONIC2_TRIG_PIN, LOW); 
  delayMicroseconds(2); 
  // Sets the trigger pin to HIGH state for 10 microseconds 
   
  digitalWrite(ULTRASONIC2_TRIG_PIN, HIGH); 
  delayMicroseconds(10); 
   
  digitalWrite(ULTRASONIC2_TRIG_PIN, LOW); 
  
  // Reads the echo pin, and returns the sound wave travel time in microseconds 
 
  distanciaS2 = pulseIn(ULTRASONIC2_ECHO_PIN, HIGH) * 0.01723;  
    if (distanciaS2 != 0) 
  { 
    lastValidValueS2 = distanciaS2; 
  } 
    // sensor 3 
  digitalWrite(ULTRASONIC3_TRIG_PIN, LOW); 
  delayMicroseconds(2); 
  // Sets the trigger pin to HIGH state for 10 microseconds 
  digitalWrite(ULTRASONIC3_TRIG_PIN, HIGH); 
  delayMicroseconds(10); 
  digitalWrite(ULTRASONIC3_TRIG_PIN, LOW); 
  
  // Reads the echo pin, and returns the sound wave travel time in microseconds 
 
  distanciaS3 = pulseIn(ULTRASONIC3_ECHO_PIN, HIGH) * 0.01723;  
} 
PAP 
SchoolBot 
void setup() 
{ 
Serial.begin(115200); 
// definir os pinos como entradas ou saídas 
pinMode(saida8, OUTPUT); 
pinMode(saida9, OUTPUT); 
pinMode(saida16, OUTPUT); 
pinMode(entrada17, INPUT); 
pinMode(ULTRASONIC1_ECHO_PIN, INPUT); 
pinMode(ULTRASONIC1_TRIG_PIN, OUTPUT);  
pinMode(ULTRASONIC2_ECHO_PIN, INPUT); 
pinMode(ULTRASONIC2_TRIG_PIN, OUTPUT);  
pinMode(ULTRASONIC3_ECHO_PIN, INPUT); 
pinMode(ULTRASONIC3_TRIG_PIN, OUTPUT); 
delay(1500);                      
// wait electronics to stabilize 
omni.i2cConnect(OMNI3MD_ADDRESS); // set i2c connection 
omni.stop();                      
// stop all motors 
omni.setI2cTimeout(0);            
// safety parameter -> I2C communication must occur every [byte timeout] x 100 
milliseconds for motor movement 
omni.setRamp(35, 900);            
// set acceleration ramp and limiar movement parameter gain[int slope, int Kl] 
slope between 0 and 100 kl->gain for necessary motor power to start movement 
omni.setMinBat(12.0);             
// Battery discharge protection voltage (Lithium 4S) 
nss.begin(9600);       
pixy.init(); 
// start serial communication at 9600bps 
// garantir que o robo começa parado 
int lin_speed = 0; 
int rot_speed = 0; 
int dir = 0; 
omni.movOmni(lin_speed, rot_speed, dir); //move motors 
delay(10); // The time for the PID control rate 
Luís Oliveira  
Técnico de Mecatrónica – Triénio 2019/2022 
 
IMP.21 – V01 
Página 91 
 
Luís Oliveira  
Técnico de Mecatrónica – Triénio 2019/2022 
 
IMP.21 – V01 
Página 92 
 
PAP 
SchoolBot 
   
} 
 
//criar a função de movimento em que o robo fica paralelo à parede 
void moveRobot2() 
{ 
      if (distanciaS3 < distancia50) // Se o sensor frontal detetar um objeto a menos de 50 cm... 
      { 
        omni.stop(); // O robô para 
      } 
      else // se não... 
      { 
 
        if (distanciaDif < -2) // Se o robô tiver inclinado para a esquerda 
        { 
          int lin_speed = 0; 
          int rot_speed = -10; 
          int dir = 0; 
          omni.movOmni(lin_speed, rot_speed, dir); //vai rodar para a direita 
          delay(10); // The time for the PID control rate 
          Serial.println("rodar direita"); // e vai mostrar no ecrã que rodou para a direita 
        } 
        else if (distanciaDif > 2) // Se o robô tiver inclinado para a direita 
        { 
          int lin_speed = 0; 
          int rot_speed = 10; 
          int dir = 0; 
          omni.movOmni(lin_speed, rot_speed, dir); //vai rodar para a esquerda 
          delay(10); // The time for the PID control rate 
          Serial.println("rodar esquerda"); // e vai mostrar no ecrã que rodou para a esquerda 
        } 
        else if (distanciaDif > -3 && distanciaDif < 3) // Se o robô tiver paralelo à parede  
            if (distanciaMin > distancia55 && distanciaMin < distancia60) // Se ele tiver entre 50 e 60 cm da parede  
            { 
              int lin_speed = 50; 
              int rot_speed = 0; 
              int dir = 60; 
 
Luís Oliveira  
Técnico de Mecatrónica – Triénio 2019/2022 
 
IMP.21 – V01 
Página 93 
 
PAP 
SchoolBot 
              omni.movOmni(lin_speed, rot_speed, dir); //este anda em frente 
              delay(10); // The time for the PID control rate 
              Serial.println("Frente");         
             } 
             else if (distanciaMin < distancia55) // Se ele tiver muito proximo da parede  
             { 
               int lin_speed = 50; 
               int rot_speed = 0; 
               int dir = 40; 
               omni.movOmni(lin_speed, rot_speed, dir); //este anda para a direita 
               delay(10); // The time for the PID control rate 
               Serial.println("direita");  
             } 
             else if (distanciaMin > distancia60) // Se ele tiver muito proximo da parede  
             { 
               int lin_speed = 50; 
               int rot_speed = 0; 
               int dir = 80; 
               omni.movOmni(lin_speed, rot_speed, dir); //este anda para a esquerda 
               delay(10); // The time for the PID control rate 
               Serial.println("esquerda");         
             } 
      } 
} 
void moveRobot1() // o robo apenas se afasta ou aproxima da parede 
{ 
  if (distanciaS3 < distancia50) // Se o sensor frontal detetar um objeto a menos de 50 cm... 
  { 
    omni.stop(); // O robô para 
  } 
  else // se não... 
  { 
    if (distanciaMin > distancia50 && distanciaMin < distancia60) // Se ele tiver entre 50 e 60 cm da parede  
    { 
      int lin_speed = 50; 
      int rot_speed = 0; 
      int dir = 60; // a parte frontal do robo foi definida como 60º 
 
Luís Oliveira  
Técnico de Mecatrónica – Triénio 2019/2022 
 
IMP.21 – V01 
Página 94 
 
PAP 
SchoolBot 
      omni.movOmni(lin_speed, rot_speed, dir); //este anda em frente 
      delay(10); // The time for the PID control rate 
      Serial.println("Frente");         
     } 
     else if (distanciaMin < distancia50) // Se ele tiver muito proximo da parede  
     { 
       int lin_speed = 50; 
       int rot_speed = 0; 
       int dir = 40; 
       omni.movOmni(lin_speed, rot_speed, dir); //este anda para a direita 
       delay(10); // The time for the PID control rate 
       Serial.println("direita");  
     } 
     else if (distanciaMin > distancia60) // Se ele tiver muito proximo da parede  
     { 
       int lin_speed = 50; 
       int rot_speed = 0; 
       int dir = 80; 
       omni.movOmni(lin_speed, rot_speed, dir); //este anda para a esquerda 
       delay(10); // The time for the PID control rate 
       Serial.println("esquerda");         
     } 
   } 
} 
 
void moveapp() // controlo feito pela app 
{ 
    if (valory < 125) 
    { 
      int lin_speed = velocidade; 
      int rot_speed = 0; 
      int dir = -angpos+60; 
      omni.movOmni(lin_speed, rot_speed, dir); //move motors 
      delay(10); // The time for the PID control rate 
     // Serial.println("Frente"); 
    } 
 
 
Luís Oliveira  
Técnico de Mecatrónica – Triénio 2019/2022 
 
IMP.21 – V01 
Página 95 
 
PAP 
SchoolBot 
     
    if (valory > 125) 
    { 
      int lin_speed = velocidade; 
      int rot_speed = 0; 
      int dir = -angneg+60; 
      omni.movOmni(lin_speed, rot_speed, dir); //move motors 
      delay(10); // The time for the PID control rate 
      //Serial.println("trás"); 
    } 
 
    // usado em caso de erro no uso do joystick 
   /* if (valory == 125){ 
       if (valorx < 125)  
       { 
        int lin_speed = vel; 
        int rot_speed = 0; 
        int dir = 90; 
        omni.movOmni(lin_speed, rot_speed, dir); //move motors 
        delay(100); // The time for the PID control rate 
       } 
        else if (valorx > 125)  
       { 
        int lin_speed = vel; 
        int rot_speed = 0; 
        int dir = 270; 
        omni.movOmni(lin_speed, rot_speed, dir); //move motors 
        delay(100); // The time for the PID control rate 
       } 
        else if (valorx == 125)  
       { 
        int lin_speed = vel; 
        int rot_speed = 0; 
        int dir = 0; 
        omni.movOmni(lin_speed, rot_speed, dir); //move motors 
        delay(100); // The time for the PID control rate 
       } 
 
Luís Oliveira  
Técnico de Mecatrónica – Triénio 2019/2022 
 
IMP.21 – V01 
Página 96 
 
PAP 
SchoolBot 
*/ 
    if (valorx == 125 && valory == 125)   
    { 
      omni.stop();      // parar todos os motores 
      delay(10); // The time for the PID control rate 
      //Serial.println("parar"); 
    } 
  delay(0); 
   
} 
 
 
void loop() 
{ 
   updateUltrasonicDistance(); 
  distanciaDif = (lastValidValueS1 - lastValidValueS2); // valor da diferenca das distancias dos sensores 
  distanciaMin = min(lastValidValueS1, lastValidValueS2); // dizer qual o sensor com a distancia mais baixa 
 
if (entrada17==0) 
{ 
  start = 0; // ativar o controlo por app 
} 
else if (entrada17==1) 
 
{ 
 start =1; // ativar o controlo automatico 
} 
 
// criação das variaveis usadas para o uso do joystick como explicado no relatório 
 veloz = sqrt(pow(valorx-125,2)+pow(valory-125,2)); 
 vel = (100 * veloz)/ 125; 
 radpos = -atan((125-(valorx))/(125-(valory))); 
 angpos = 180/PI*(radpos); 
 radneg = atan(((valorx)-125)/(125-(valory)))+ PI; 
 angneg = 180/PI*(radneg); 
 velocidade = 0; 
 
 
Luís Oliveira  
Técnico de Mecatrónica – Triénio 2019/2022 
 
IMP.21 – V01 
Página 97 
 
PAP 
SchoolBot 
// comunicação com a app 
  while (nss.available()) { 
    delay(3); 
    val[0] = nss.read(); 
    readString += val[0]; 
    val[1] = nss.read(); 
    readString += val[1]; 
    valorx = val[0]; 
    valory = val[1]; 
 
  } 
// uma vez que a velocidade maxima é 100, isto garante que a velocidade não o exceda 
    if (vel>50) 
    { 
       velocidade = 50; 
    } 
    else  
    { 
       velocidade = vel; 
    } 
//Serial.print(String(distanciaS1) + "cm\n" + distanciaS2 + "cm\n" + distanciaS3 + "cm\n"); 
//Serial.print(String(lastValidValueS1) + "cm1  " + lastValidValueS2 + "cm2  ");  
//Serial.print(String(distanciaDif)); 
   int i;  
   // grab blocks! 
   pixy.ccc.getBlocks(); 
 
// saber em que numero (da etiqueta) a cor foi guardada 
   pixyColor color = (pixyColor)pixy.ccc.blocks[i].m_signature; 
 
 
 
 
  if (start = 0) // Se o utilizador não tiver carregado no botão começar 
  { 
    moveapp(); // o controlo da app está ativado  
  } 
 
Luís Oliveira  
Técnico de Mecatrónica – Triénio 2019/2022 
 
IMP.21 – V01 
Página 98 
 
PAP 
SchoolBot 
  else // se não consoante a cor este.... 
  { 
    switch (color) 
    { 
      case colorGreen: //verde 
      if (salaGreen == 0) 
      { 
        moveRobot1(); // ativa um tipo de movimentação definido anteriormente se esta cor ja tiver sido detetada 
      } 
      else // se não, este detetar a cor pela primeira vez 
      { 
        // vai se preparar para mostrar o video 
        Serial.println("cor verde detetada"); 
        omni.stop(); 
        delay(2000); 
        omni.movOmni(0,-30,0); //(lin_speed,rot_speed,dir) esquerda 
        delay(990); 
        omni.stop(); 
       // delay(2000); 
       // e este vai dizer ao rpi qual a sala detetada 
        digitalWrite(saida8 , HIGH); 
        digitalWrite(saida9 , LOW); 
        digitalWrite(saida16 , LOW); 
        delay(5000); // tempo do video 
        omni.movOmni(0,30,0); //move motors direita 
        delay(1010); 
        omni.stop(); 
       // salaGreen = 0; 
        mov = 2; 
        //  omni.movOmni(30,0,60); //(lin_speed,rot_speed,dir) 
        //delay(5000); 
      } 
        break; 
       
      case colorRed: // red 
      if (salaRed == 0) 
      { 
 
Luís Oliveira  
Técnico de Mecatrónica – Triénio 2019/2022 
 
IMP.21 – V01 
Página 99 
 
PAP 
SchoolBot 
        moveRobot1(); 
      } 
      else 
      { 
                Serial.println("cor vermelho detetada"); 
        omni.stop(); 
        delay(2000); 
        omni.movOmni(0,-30,0); //(lin_speed,rot_speed,dir) esquerda 
        delay(990); 
        omni.stop(); 
       // delay(2000); 
        digitalWrite(saida8 , HIGH);//Define ledPin como HIGH, ligando o LED 
        digitalWrite(saida9 , LOW);//Define ledPin como HIGH, ligando o LED 
        digitalWrite(saida16 , HIGH);//Define ledPin como HIGH, ligando o LED 
 
        delay(5000); // tempo do video 
        omni.movOmni(0,30,0); //move motors direita 
        delay(1030); 
        omni.stop(); 
      //  salaRed = 0; 
        mov = 1; 
  
      //  omni.movOmni(30,0,60); //(lin_speed,rot_speed,dir) 
        //delay(5000); 
      } 
        break; 
         
        case colorBlue: // azul 
      if (salaBlue == 0) //0 
      { 
       moveRobot1(); 
      } 
      else 
      { 
        Serial.println("cor azul detetada"); 
        omni.stop(); 
        delay(2000); 
 
Luís Oliveira  
Técnico de Mecatrónica – Triénio 2019/2022 
 
IMP.21 – V01 
Página 100 
 
PAP 
SchoolBot 
        omni.movOmni(0,-30,0); //(lin_speed,rot_speed,dir) esquerda 
        delay(990); 
        omni.stop(); 
       // delay(2000); 
        digitalWrite(saida8 , HIGH); 
        digitalWrite(saida9 , HIGH); 
        digitalWrite(saida16 , LOW); 
 
        delay(5000); // tempo do video 
        omni.movOmni(0,30,0); //move motors direita 
        delay(1020); 
        omni.stop(); 
       // salaBlue = 0; 
        mov = 1; 
      //  omni.movOmni(30,0,60); //(lin_speed,rot_speed,dir) 
        //delay(5000); 
      } 
        break; 
              case colorYellow: // red 
      if (salaYellow == 0) 
      { 
        moveRobot1(); 
      } 
      else 
      { 
          Serial.println("cor amerela detetada"); 
         omni.stop(); 
        delay(2000); 
        omni.movOmni(0,-30,0); //(lin_speed,rot_speed,dir) esquerda 
        delay(1500); 
        omni.stop(); 
        digitalWrite(saida8 , HIGH); 
        digitalWrite(saida9 , HIGH); 
        digitalWrite(saida16 , HIGH); 
 
        delay(4000); // tempo do video 
        omni.movOmni(0,30,0); //move motors direita 
 
Luís Oliveira  
Técnico de Mecatrónica – Triénio 2019/2022 
 
IMP.21 – V01 
Página 101 
 
PAP 
SchoolBot 
        delay(500); 
        omni.stop(); 
        delay(1900); 
        omni.movOmni(50,0,60 ); //(lin_speed,rot_speed,dir) 
        delay(1900); 
        omni.movOmni(0,-30,0); //(lin_speed,rot_speed,dir) esquerda 
        delay(700); 
        omni.stop(); 
    
      /*  mov = 2; 
        salaGreen = 1; 
        salaRed = 1;  
        salaBlue = 1; */ 
 
      } 
            break; 
 
     case colorroxo: // CORREDOR LATERAL 
  
 
  
      moveRobot1(); 
       delay(8000); 
 
  
           break; 
           // se nenhuma cor for detetada este vai se movimentar 
    default: 
        digitalWrite(saida8 , LOW);//Define ledPin como HIGH, ligando o LED 
        digitalWrite(saida9 , LOW);//Define ledPin como HIGH, ligando o LED 
        digitalWrite(saida16 , LOW);//Define ledPin como HIGH, ligando o LED 
 
         
    if (mov==1) 
    { 
      Serial.println("nenhuma cor detetada");   
      moveRobot1(); 
PAP 
SchoolBot 
} 
else 
{ 
moveRobot2(); 
} 
break; 
} 
} 
delay(100); // Delay a little bit to improve simulation performance 
}
