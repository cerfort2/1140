

int E_ON = 22;
int E_OFF = 24;// Pin connected to the LED
int S_ON = 26;
int S_OFF = 28;
int B_ON = 30;
int B_OFF = 32;

float result = 0;
int manualmode = 1;
double ek_prev = 0.0;
double e_k = 0.0;
float manualcommandedspeed = 0;
float currentSpeed = 0;
double ctcSpeed = 0.0;
double u_k = 0.0;
double uk_prev = 0.0;
double kp = 400;
double ki = 20;
float power = 0.0;
bool brakeFailure = false;
bool signalFailure = false;
bool engineFailure = false;
int eBrake = 0;
int serviceBrake = 0;
int authority = 0;
int rightdoor = 0;
int leftdoor = 0;
int exterior = 0;
int interior = 0;
int e_failure = 0;
int s_failure = 0;
int b_failure = 0;
int temperature = 0;

String data;

#include <LCD_I2C.h>
LCD_I2C lcd(0x20, 20, 4);

uint8_t happy[8] =
{
    0b00000,
    0b10001,
    0b00000,
    0b00000,
    0b10001,
    0b01110,
    0b00000,
    0b00000,
};

void setup() {
  pinMode(E_ON, OUTPUT);
  pinMode(E_OFF,OUTPUT);
  pinMode(S_ON,OUTPUT);
  pinMode(S_OFF,OUTPUT);
  pinMode(B_ON,OUTPUT);
  pinMode(B_OFF,OUTPUT);
  lcd.begin(); // If you are using more I2C devices using the Wire library use lcd.begin(false)
// this stop the library(LCD_I2C) from calling Wire.begin()
  lcd.backlight();

  Serial.begin(115200); // Same baud rate as the Python code
}

double calculatePower() 
{
  
    if (manualmode == 1) 
    {
        ek_prev = e_k;
        e_k = (manualcommandedspeed - currentSpeed);
        u_k = (0.05 / 2) * (e_k + ek_prev);
        power = (e_k * kp - ki * u_k);
    } 
    else 
    {
        ek_prev = e_k;
        e_k = (ctcSpeed - currentSpeed);
        u_k = (0.05 / 2) * (e_k + ek_prev);
        power = (e_k * kp - ki * u_k);
    }

    
    if (power > 120000) 
    {
        power = 120000;
    }
    
    
    if (brakeFailure || signalFailure || engineFailure || eBrake == 1 || power < 0 || serviceBrake == 1 || authority <= 0) 
    {
        power = 0;
    }

    
    if (power < 0)
    {
      power = 0;
    }
    
    return power;
    

  

  return currentSpeed - ctcSpeed;
    
}

void LED_logic()
{
  if (e_failure == 1 && s_failure == 1 && b_failure == 1) {
    digitalWrite(E_ON, LOW);
    digitalWrite(E_OFF, HIGH);
    digitalWrite(S_ON, LOW);
    digitalWrite(S_OFF, HIGH);
    digitalWrite(B_ON, LOW);
    digitalWrite(B_OFF, HIGH);
  } else if (e_failure == 1 && s_failure == 1 && b_failure == 0) {
    digitalWrite(E_ON, LOW);
    digitalWrite(E_OFF, HIGH);
    digitalWrite(S_ON, LOW);
    digitalWrite(S_OFF, HIGH);
    digitalWrite(B_ON, HIGH);
    digitalWrite(B_OFF, LOW);
  } else if (e_failure == 1 && s_failure == 0 && b_failure == 1) {
    digitalWrite(E_ON, LOW);
    digitalWrite(E_OFF, HIGH);
    digitalWrite(S_ON, HIGH);
    digitalWrite(S_OFF, LOW);
    digitalWrite(B_ON, LOW);
    digitalWrite(B_OFF, HIGH);
  } else if (e_failure == 1 && s_failure == 0 && b_failure == 0) {
    digitalWrite(E_ON, LOW);
    digitalWrite(E_OFF, HIGH);
    digitalWrite(S_ON, HIGH);
    digitalWrite(S_OFF, LOW);
    digitalWrite(B_ON, HIGH);
    digitalWrite(B_OFF, LOW);
  } else if (e_failure == 0 && s_failure == 1 && b_failure == 1) {
    digitalWrite(E_ON, HIGH);
    digitalWrite(E_OFF, LOW);
    digitalWrite(S_ON, LOW);
    digitalWrite(S_OFF, HIGH);
    digitalWrite(B_ON, LOW);
    digitalWrite(B_OFF, HIGH);
  } else if (e_failure == 0 && s_failure == 1 && b_failure == 0) {
    digitalWrite(E_ON, HIGH);
    digitalWrite(E_OFF, LOW);
    digitalWrite(S_ON, LOW);
    digitalWrite(S_OFF, HIGH);
    digitalWrite(B_ON, HIGH);
    digitalWrite(B_OFF, LOW);
  } else if (e_failure == 0 && s_failure == 0 && b_failure == 1) {
    digitalWrite(E_ON, HIGH);
    digitalWrite(E_OFF, LOW);
    digitalWrite(S_ON, HIGH);
    digitalWrite(S_OFF, LOW);
    digitalWrite(B_ON, LOW);
    digitalWrite(B_OFF, HIGH);
  } else {
    digitalWrite(E_ON, HIGH);
    digitalWrite(E_OFF, LOW);
    digitalWrite(S_ON, HIGH);
    digitalWrite(S_OFF, LOW);
    digitalWrite(B_ON, HIGH);
    digitalWrite(B_OFF, LOW);

  }
}

void LCD_logic()
{
  String right_door, left_door, exterior_lights, interior_lights;
  if(rightdoor == 1)
  {
    right_door = "ON";
  }
  else
  {
    right_door = "OFF";
  }

  if(leftdoor == 1)
  {
    left_door = "ON";
  }
  else
  {
    left_door = "OFF";
  }

  if(exterior == 1)
  {
    exterior_lights = "ON";
  }
  else
  {
    exterior_lights = "OFF";
  }

  if(interior == 1)
  {
    interior_lights = "ON";
  }
  else
  {
    interior_lights = "OFF";
  }
  lcd.setCursor(0,0);
  lcd.print("Right Door:" + right_door); // You can make spaces using well... spaces // Or setting the cursor in the desired position.

  lcd.setCursor(0,1);
  lcd.print("Left Door:" + left_door);

  lcd.setCursor(0,2);
  lcd.print("Exterior Lights:" + exterior_lights);

  lcd.setCursor(0,3);
  lcd.print("Interior Lights:" + interior_lights);

  lcd.setCursor(17,0);
  String temp = String(temperature);
  lcd.print(temp);

  lcd.setCursor(19,0);
  lcd.print("F");
  
  


  delay(500);
}

void loop() {


    if (Serial.available() > 0) {
    String inputString = Serial.readStringUntil('\n'); // Read the string until newline ('\n') character
    inputString.trim(); // Remove leading/trailing whitespace

    int values[15];
    int parse = 0;

    char *token = strtok(const_cast<char*>(inputString.c_str()), ",");

    while (token != NULL && parse < 15) {
      values[parse] = atoi(token); // Convert token to integer
      parse++;
      token = strtok(NULL, ",");
    }

    if (parse == 15) {
      manualmode = values[0];
      currentSpeed = values[1];
      manualcommandedspeed = values[2];
      ctcSpeed = values[3];
      serviceBrake = values[4];
      eBrake = values[5];
      authority = values[6];
      rightdoor = values[7];
      leftdoor = values[8];
      exterior = values[9];
      interior = values[10];
      e_failure = values[11];
      s_failure = values[12];
      b_failure = values[13];
      temperature = values[14];
    }
  }
  

  //values = f"{self.mode_as_int},{self.currentSpeed},{self.manualcommandedspeed},{self.ctcSpeed},{self.serviceb},{self.emergencybrake},{self.authority},{self.RD},{self.LD},{self.e_light},{self.i_light},{self.e_failure},{self.s_failure},{self.b_failure}\n"

  LED_logic();

  LCD_logic();

  result = calculatePower();
  Serial.println(result);
  delay(1000);
  
}