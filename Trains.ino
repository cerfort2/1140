#include <LiquidCrystal_I2C.h>
#include <Wire.h> 

#if defined(ARDUINO) && ARDUINO >= 100
#define printByte(args) write(args);
#else
#define printByte(args) print(args, BYTE);
#endif

String choice;
String toVal;
String fromVal;

const int greenLineSize = 151;
bool greenLine[greenLineSize];

const int switchAmountGreen = 5;
String greenLineSwitches[switchAmountGreen];

const int lightsAmountGreen = 10;
String greenLineLights[lightsAmountGreen];

uint8_t line[8] = {0x4, 0x4, 0x4, 0x4, 0x4, 0x4, 0x4, 0x4}; //down line
uint8_t switchMid[8] = {0x11, 0x0A, 0x04, 0x4, 0x4, 0x4, 0x4, 0x4}; //switch mid
uint8_t switchLeft[8] = {0x0, 0x1E, 0x18, 0x14, 0x12, 0x01, 0x01, 0x01}; //switch left arrow
uint8_t switchRight[8] = {0x0, 0x0F, 0x03, 0x05, 0x09, 0x10, 0x10, 0x10}; //switch right arrow
uint8_t fill[8] = {0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F}; //fill block
uint8_t clears[8] = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00}; //fill block

const int red = 29;
const int green = 39;

LiquidCrystal_I2C lcd(0x20, 20, 4);
void setup() 
{
  Serial.begin(115200);
  lcd.init();
  lcd.backlight();
  lcd.createChar(0, line);
  lcd.createChar(1, switchMid);
  lcd.createChar(2, switchLeft);
  lcd.createChar(3, switchRight);
  lcd.createChar(4, fill);
  lcd.createChar(5, clears);
  lcd.home();

  greenLineSwitches[0] = "1";
  greenLineSwitches[1] = "1";
  greenLineSwitches[2] = "1";
  greenLineSwitches[3] = "1";
  greenLineSwitches[4] = "1";

  greenLineLights[0] = "1";
  greenLineLights[1] = "1";
  greenLineLights[2] = "1";
  greenLineLights[3] = "1";
  greenLineLights[4] = "1";
  greenLineLights[5] = "1";
  greenLineLights[6] = "1";
  greenLineLights[7] = "1";
  greenLineLights[8] = "1";
  greenLineLights[9] = "1";

  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);

  //Setting the Display default
  lcd.print("Crossroad");
  lcd.setCursor(9,0);
  lcd.write(0);
  lcd.setCursor(9,1);
  lcd.write(0);
  lcd.setCursor(9,2);
  lcd.write(0);
  lcd.setCursor(9,3);
  lcd.write(0);
  lcd.setCursor(12,0);
  lcd.print("Switch");
  lcd.setCursor(15,2);
  lcd.write(1);
  lcd.setCursor(14,1);
  lcd.write(2);
  lcd.setCursor(16,1);
  lcd.write(3);
}

void loop() 
{
  if(Serial.available() > 0)
  {
    choice = Serial.readString();
  }
  if(choice == "R")
  {
    switchRights();
    choice = "";
  }
  else if(choice == "L")
  {
    switchLefts();
    choice = "";
  }
  else if(choice == "G")
  {
    lights();
    choice = "";
  }
  else if(choice == "O")
  {
    crossroadOn();
    choice = "";
  }
  else if(choice == "F")
  {
    crossroadOff();
    choice = "";
  }
  else if(choice == "C")
  {
    getAndSendData();
    choice = "";
  }
}

void getAndSendData()
{
  char received;
  int i = 0;
  while(true)
  {
    if(Serial.available() > 0)
    {
      received = Serial.read();

      if (received == '\0')
      {
        break;  // End of data
      }
      greenLine[i] = (received == '1');
      i++;
    }
  }
  plcLogic();
  //Code to send back switch states
  String sentSwitches;
  String sentLights;
  for(int i = 0; i < switchAmountGreen; i++)
  {
    sentSwitches += greenLineSwitches[i];
  }
  Serial.print(sentSwitches);
  delay(1250);
  for(int i = 0; i < lightsAmountGreen; i++)
  {
    sentLights += greenLineLights[i];
  }
  Serial.print(sentLights);
}

void plcLogic()
{
  /*
   * Arrays from [0]-[31] and [149] belongs to Wayside 1
   * Array from [32]-[72] and [150] belong to Wayside 2
   * Array from [73]-[100] belong to Wayside 3
   * Array from [101]-[148] belong to Wayside 4
   */
   //Logic for Switch 1 on J62 DC for 000, 100, 011: 1st = K, 2nd = J, 3rd = Yard
   if(greenLine[150] and not (greenLine[61] or greenLine[62] or greenLine[63]))//Anything leaving Yard takes priority unless train in front 001/011
   {
      greenLineSwitches[0] = "1";
      greenLineLights[0] = "0";
      greenLineLights[1] = "1";
   }
   else if((greenLine[59] or greenLine[60]) and not (greenLine[61] or greenLine[62] or greenLine[63]) and not greenLine[150]) //Train only in J60 going to repeat 010
   {
      greenLineSwitches[0] = "0";
      greenLineLights[0] = "1";
      greenLineLights[1] = "0";
   }
   else if(greenLine[150] and (greenLine[61] or greenLine[62] or greenLine[63])) //101
   {
      greenLineSwitches[0] = "1";
      greenLineLights[0] = "1";
      greenLineLights[1] = "1";
   }
   else if((greenLine[59] or greenLine[60]) and (greenLine[61] or greenLine[62] or greenLine[63]) and not greenLine[150]) //110
   {
      greenLineSwitches[0] = "0";
      greenLineLights[0] = "1";
      greenLineLights[1] = "1";
   }
   else if((greenLine[59] or greenLine[60]) and (greenLine[61] or greenLine[62] or greenLine[63]) and greenLine[150]) //111
   {
      greenLineSwitches[0] = "1";
      greenLineLights[0] = "1";
      greenLineLights[1] = "1";
   }
   
   //Logic for Switch 2 on N77 DC is 000, 001: 1st = M, 2nd = N, 3rd = R
   if((greenLine[73] or greenLine[74] or greenLine[75]) and not (greenLine[76] or greenLine[77] or greenLine[78] or greenLine[79] or greenLine[80] or greenLine[81] or greenLine[82] or greenLine[83] or greenLine[84] or greenLine[85]) and not greenLine[100] and not (greenLine[99] or greenLine[98])) //100
   {
      greenLineSwitches[1] = "1";
      greenLineLights[2] = "0";
      greenLineLights[3] = "1";
   }
   else if((greenLine[73] or greenLine[74] or greenLine[75]) and not (greenLine[76] or greenLine[77] or greenLine[78] or greenLine[79] or greenLine[80] or greenLine[81] or greenLine[82] or greenLine[83] or greenLine[84] or greenLine[85]) and greenLine[100]) //101
   {
      greenLineSwitches[1] = "1";
      greenLineLights[2] = "0";
      greenLineLights[3] = "1";
   }
   else if((greenLine[73] or greenLine[74] or greenLine[75]) and (greenLine[76] or greenLine[77] or greenLine[78] or greenLine[79] or greenLine[80] or greenLine[81] or greenLine[82] or greenLine[83] or greenLine[84] or greenLine[85]) and not greenLine[100]) //110
   {
      greenLineSwitches[1] = "0";
      greenLineLights[2] = "1";
      greenLineLights[3] = "0";
   }
   else if((greenLine[73] or greenLine[74] or greenLine[75]) and (greenLine[76] or greenLine[77] or greenLine[78] or greenLine[79] or greenLine[80] or greenLine[81] or greenLine[82] or greenLine[83] or greenLine[84] or greenLine[85]) and greenLine[100]) //111
   {
      greenLineSwitches[1] = "0";
      greenLineLights[2] = "1";
      greenLineLights[3] = "1";
   }
   else if(not(greenLine[73] or greenLine[74] or greenLine[75]) and (greenLine[76] or greenLine[77] or greenLine[78] or greenLine[79] or greenLine[80] or greenLine[81] or greenLine[82] or greenLine[83] or greenLine[84] or greenLine[85]) and not greenLine[100]) //010
   {
      greenLineSwitches[1] = "0";
      greenLineLights[2] = "1";
      greenLineLights[3] = "0";
   }
   else if(not(greenLine[73] or greenLine[74] or greenLine[75]) and (greenLine[76] or greenLine[77] or greenLine[78] or greenLine[79] or greenLine[80] or greenLine[81] or greenLine[82] or greenLine[83] or greenLine[84] or greenLine[85]) and greenLine[100]) //011
   {
      greenLineSwitches[1] = "0";
      greenLineLights[2] = "1";
      greenLineLights[3] = "1";
   }
    
   //Logic for Switch 3 on N85 DC is 000,010: 1st = N, 2nd = O-P, 3rd = Q - Only allow 1 train in the loop at a time
   if((greenLine[76] or greenLine[77] or greenLine[78] or greenLine[79] or greenLine[80] or greenLine[81] or greenLine[82] or greenLine[83] or greenLine[84] or greenLine[85]) and not (greenLine[85] or greenLine[86] or greenLine[87] or greenLine[88] or greenLine[89] or greenLine[90] or greenLine[91] or greenLine[92] or greenLine[93] or greenLine[94] or greenLine[95] or greenLine[96]) and not (greenLine[97] or greenLine[98] or greenLine[99])) //100
   {
      greenLineSwitches[2] = "0";
      greenLineLights[4] = "0";
      greenLineLights[5] = "1";
   }
   else if((greenLine[76] or greenLine[77] or greenLine[78] or greenLine[79] or greenLine[80] or greenLine[81] or greenLine[82] or greenLine[83] or greenLine[84] or greenLine[85]) and not (greenLine[85] or greenLine[86] or greenLine[87] or greenLine[88] or greenLine[89] or greenLine[90] or greenLine[91] or greenLine[92] or greenLine[93] or greenLine[94] or greenLine[95] or greenLine[96]) and (greenLine[97] or greenLine[98] or greenLine[99])) //101
   {
      greenLineSwitches[2] = "0";
      greenLineLights[4] = "0";
      greenLineLights[5] = "1";
   }
   else if(not(greenLine[76] or greenLine[77] or greenLine[78] or greenLine[79] or greenLine[80] or greenLine[81] or greenLine[82] or greenLine[83] or greenLine[84] or greenLine[85]) and not (greenLine[85] or greenLine[86] or greenLine[87] or greenLine[88] or greenLine[89] or greenLine[90] or greenLine[91] or greenLine[92] or greenLine[93] or greenLine[94] or greenLine[95] or greenLine[96]) and (greenLine[97] or greenLine[98] or greenLine[99])) //001
   {
      greenLineSwitches[2] = "1";
      greenLineLights[4] = "1";
      greenLineLights[5] = "0";
   }
   else if(not(greenLine[76] or greenLine[77] or greenLine[78] or greenLine[79] or greenLine[80] or greenLine[81] or greenLine[82] or greenLine[83] or greenLine[84] or greenLine[85]) and (greenLine[85] or greenLine[86] or greenLine[87] or greenLine[88] or greenLine[89] or greenLine[90] or greenLine[91] or greenLine[92] or greenLine[93] or greenLine[94] or greenLine[95] or greenLine[96]) and (greenLine[97] or greenLine[98] or greenLine[99])) //011
   {
      greenLineSwitches[2] = "1";
      greenLineLights[4] = "1";
      greenLineLights[5] = "0";
   }
   else if((greenLine[76] or greenLine[77] or greenLine[78] or greenLine[79] or greenLine[80] or greenLine[81] or greenLine[82] or greenLine[83] or greenLine[84] or greenLine[85]) and (greenLine[85] or greenLine[86] or greenLine[87] or greenLine[88] or greenLine[89] or greenLine[90] or greenLine[91] or greenLine[92] or greenLine[93] or greenLine[94] or greenLine[95] or greenLine[96]) and not (greenLine[97] or greenLine[98] or greenLine[99])) //110
   {
      greenLineSwitches[2] = "1";
      greenLineLights[4] = "1";
      greenLineLights[5] = "1";
   }
   else if((greenLine[76] or greenLine[77] or greenLine[78] or greenLine[79] or greenLine[80] or greenLine[81] or greenLine[82] or greenLine[83] or greenLine[84] or greenLine[85]) and (greenLine[85] or greenLine[86] or greenLine[87] or greenLine[88] or greenLine[89] or greenLine[90] or greenLine[91] or greenLine[92] or greenLine[93] or greenLine[94] or greenLine[95] or greenLine[96]) and (greenLine[97] or greenLine[98] or greenLine[99])) //111
   {
      greenLineSwitches[2] = "0";
      greenLineLights[4] = "1";
      greenLineLights[5] = "1";
   }

   //Logic for Switch 4 on G29 DC is 000, 010: 1st = F-D, 2nd = G, 3rd = Z
   if((greenLine[12] or greenLine[13] or greenLine[14] or greenLine[15] or greenLine[16] or greenLine[17] or greenLine[18] or greenLine[19] or greenLine[20] or greenLine[21] or greenLine[22] or greenLine[23] or greenLine[24] or greenLine[25] or greenLine[26] or greenLine[27] or greenLine[28]) and not (greenLine[29] or greenLine[30] or greenLine[31]) and not (greenLine[147] or greenLine[148] or greenLine[149])) //100
   {
      greenLineSwitches[3] = "0";
      greenLineLights[6] = "1";
      greenLineLights[7] = "0";
   }
   else if((greenLine[12] or greenLine[13] or greenLine[14] or greenLine[15] or greenLine[16] or greenLine[17] or greenLine[18] or greenLine[19] or greenLine[20] or greenLine[21] or greenLine[22] or greenLine[23] or greenLine[24] or greenLine[25] or greenLine[26] or greenLine[27] or greenLine[28]) and not (greenLine[29] or greenLine[30] or greenLine[31]) and (greenLine[147] or greenLine[148] or greenLine[149])) //101
   {
      greenLineSwitches[3] = "0";
      greenLineLights[6] = "1";
      greenLineLights[7] = "0";
   }
   else if((greenLine[12] or greenLine[13] or greenLine[14] or greenLine[15] or greenLine[16] or greenLine[17] or greenLine[18] or greenLine[19] or greenLine[20] or greenLine[21] or greenLine[22] or greenLine[23] or greenLine[24] or greenLine[25] or greenLine[26] or greenLine[27] or greenLine[28]) and (greenLine[29] or greenLine[30] or greenLine[31]) and not (greenLine[147] or greenLine[148] or greenLine[149])) //110
   {
      greenLineSwitches[3] = "0";
      greenLineLights[6] = "1";
      greenLineLights[7] = "1";
   }
   else if((greenLine[12] or greenLine[13] or greenLine[14] or greenLine[15] or greenLine[16] or greenLine[17] or greenLine[18] or greenLine[19] or greenLine[20] or greenLine[21] or greenLine[22] or greenLine[23] or greenLine[24] or greenLine[25] or greenLine[26] or greenLine[27] or greenLine[28]) and (greenLine[29] or greenLine[30] or greenLine[31]) and (greenLine[147] or greenLine[148] or greenLine[149])) //111
   {
      greenLineSwitches[3] = "0";
      greenLineLights[6] = "1";
      greenLineLights[7] = "1";
   }
   else if(not(greenLine[12] or greenLine[13] or greenLine[14] or greenLine[15] or greenLine[16] or greenLine[17] or greenLine[18] or greenLine[19] or greenLine[20] or greenLine[21] or greenLine[22] or greenLine[23] or greenLine[24] or greenLine[25] or greenLine[26] or greenLine[27] or greenLine[28]) and not (greenLine[29] or greenLine[30] or greenLine[31]) and (greenLine[147] or greenLine[148] or greenLine[149]) and not (greenLine[0] or greenLine[1])) //001
   {
      greenLineSwitches[3] = "1";
      greenLineLights[6] = "0";
      greenLineLights[7] = "1";
   }
   else if(not(greenLine[12] or greenLine[13] or greenLine[14] or greenLine[15] or greenLine[16] or greenLine[17] or greenLine[18] or greenLine[19] or greenLine[20] or greenLine[21] or greenLine[22] or greenLine[23] or greenLine[24] or greenLine[25] or greenLine[26] or greenLine[27] or greenLine[28]) and (greenLine[29] or greenLine[30] or greenLine[31]) and (greenLine[147] or greenLine[148] or greenLine[149])) //011
   {
      greenLineSwitches[3] = "1";
      greenLineLights[6] = "0";
      greenLineLights[7] = "1";
   }

   //Logic for Switch 5 on D13 DC is 000,010: 1st = D-F, 2nd = B-C, 3rd = A - Only allow 1 train in the loop at a time
   if((greenLine[12] or greenLine[13] or greenLine[14] or greenLine[15] or greenLine[16] or greenLine[17] or greenLine[18] or greenLine[19] or greenLine[20] or greenLine[21] or greenLine[22] or greenLine[23] or greenLine[24] or greenLine[25] or greenLine[26] or greenLine[27] or greenLine[28]) and not (greenLine[3] or greenLine[4] or greenLine[5] or greenLine[6] or greenLine[7] or greenLine[8] or greenLine[9] or greenLine[10] or greenLine[11]) and not (greenLine[0] or greenLine[1] or greenLine[2])) //100
   {
      greenLineSwitches[4] = "0";
      greenLineLights[8] = "0";
      greenLineLights[9] = "1";
   }
   else if((greenLine[12] or greenLine[13] or greenLine[14] or greenLine[15] or greenLine[16] or greenLine[17] or greenLine[18] or greenLine[19] or greenLine[20] or greenLine[21] or greenLine[22] or greenLine[23] or greenLine[24] or greenLine[25] or greenLine[26] or greenLine[27] or greenLine[28]) and not (greenLine[3] or greenLine[4] or greenLine[5] or greenLine[6] or greenLine[7] or greenLine[8] or greenLine[9] or greenLine[10] or greenLine[11]) and (greenLine[0] or greenLine[1] or greenLine[2])) //101
   {
      greenLineSwitches[4] = "0";
      greenLineLights[8] = "0";
      greenLineLights[9] = "1";
   }
   else if((greenLine[12] or greenLine[13] or greenLine[14] or greenLine[15] or greenLine[16] or greenLine[17] or greenLine[18] or greenLine[19] or greenLine[20] or greenLine[21] or greenLine[22] or greenLine[23] or greenLine[24] or greenLine[25] or greenLine[26] or greenLine[27] or greenLine[28]) and (greenLine[3] or greenLine[4] or greenLine[5] or greenLine[6] or greenLine[7] or greenLine[8] or greenLine[9] or greenLine[10] or greenLine[11]) and not (greenLine[0] or greenLine[1] or greenLine[2])) //110
   {
      greenLineSwitches[4] = "0";
      greenLineLights[8] = "1";
      greenLineLights[9] = "1";
   }
   else if((greenLine[12] or greenLine[13] or greenLine[14] or greenLine[15] or greenLine[16] or greenLine[17] or greenLine[18] or greenLine[19] or greenLine[20] or greenLine[21] or greenLine[22] or greenLine[23] or greenLine[24] or greenLine[25] or greenLine[26] or greenLine[27] or greenLine[28]) and (greenLine[3] or greenLine[4] or greenLine[5] or greenLine[6] or greenLine[7] or greenLine[8] or greenLine[9] or greenLine[10] or greenLine[11]) and (greenLine[0] or greenLine[1] or greenLine[2])) //111
   {
      greenLineSwitches[4] = "0";
      greenLineLights[8] = "1";
      greenLineLights[9] = "1";
   }
   else if(not(greenLine[12] or greenLine[13] or greenLine[14] or greenLine[15] or greenLine[16] or greenLine[17] or greenLine[18] or greenLine[19] or greenLine[20] or greenLine[21] or greenLine[22] or greenLine[23] or greenLine[24] or greenLine[25] or greenLine[26] or greenLine[27] or greenLine[28]) and not (greenLine[3] or greenLine[4] or greenLine[5] or greenLine[6] or greenLine[7] or greenLine[8] or greenLine[9] or greenLine[10] or greenLine[11]) and (greenLine[0] or greenLine[1] or greenLine[2])) //001
   {
      greenLineSwitches[4] = "1";
      greenLineLights[8] = "1";
      greenLineLights[9] = "0";
   }
   else if(not(greenLine[12] or greenLine[13] or greenLine[14] or greenLine[15] or greenLine[16] or greenLine[17] or greenLine[18] or greenLine[19] or greenLine[20] or greenLine[21] or greenLine[22] or greenLine[23] or greenLine[24] or greenLine[25] or greenLine[26] or greenLine[27] or greenLine[28]) and (greenLine[3] or greenLine[4] or greenLine[5] or greenLine[6] or greenLine[7] or greenLine[8] or greenLine[9] or greenLine[10] or greenLine[11]) and (greenLine[0] or greenLine[1] or greenLine[2])) //011
   {
      greenLineSwitches[4] = "1";
      greenLineLights[8] = "1";
      greenLineLights[9] = "0";
   }
}

//Code below is set and stone

void switchLefts()
{
  Serial.setTimeout(1000);
  fromVal = Serial.readString();
  Serial.setTimeout(1000);
  toVal = Serial.readString();

  //Clears the from value area
  lcd.setCursor(14,3);
  lcd.write(5);
  lcd.setCursor(15,3);
  lcd.write(5);
  lcd.setCursor(16,3);
  lcd.write(5);
  lcd.setCursor(17,3);
  lcd.write(5);

  //Clears current toVals
  lcd.setCursor(11,2);
  lcd.write(5);
  lcd.setCursor(12,2);
  lcd.write(5);
  lcd.setCursor(13,2);
  lcd.write(5);
  lcd.setCursor(14,2);
  lcd.write(5);

  //Writes the switches
  lcd.setCursor(16,1);
  lcd.write(5);
  lcd.setCursor(14,1);
  lcd.write(2);
  lcd.setCursor(11,2);
  lcd.print(toVal);
  lcd.setCursor(14,3);
  lcd.print(fromVal);

  //Clears the toside switch letters
  lcd.setCursor(16,2);
  lcd.write(5);
  lcd.setCursor(17,2);
  lcd.write(5);
  lcd.setCursor(18,2);
  lcd.write(5);
  lcd.setCursor(19,2);
  lcd.write(5);
}
void switchRights()
{
  Serial.setTimeout(1000);
  fromVal = Serial.readString();
  Serial.setTimeout(1000);
  toVal = Serial.readString();

  //Clears the from value area
  lcd.setCursor(14,3);
  lcd.write(5);
  lcd.setCursor(15,3);
  lcd.write(5);
  lcd.setCursor(16,3);
  lcd.write(5);
  lcd.setCursor(17,3);
  lcd.write(5);

  //Clears current toVals
  lcd.setCursor(16,2);
  lcd.write(5);
  lcd.setCursor(17,2);
  lcd.write(5);
  lcd.setCursor(18,2);
  lcd.write(5);
  lcd.setCursor(19,2);
  lcd.write(5);
  
  //Writes the switches
  lcd.setCursor(14,1);
  lcd.write(5);
  lcd.setCursor(16,1);
  lcd.write(3);
  lcd.setCursor(16,2);
  lcd.print(toVal);
  lcd.setCursor(14,3);
  lcd.print(fromVal);

  //Clears the toside switch letters
  lcd.setCursor(11,2);
  lcd.write(5);
  lcd.setCursor(12,2);
  lcd.write(5);
  lcd.setCursor(13,2);
  lcd.write(5);
  lcd.setCursor(14,2);
  lcd.write(5);
}
void lights()
{
  while(Serial.available() == 0) {} 
  byte recieved = Serial.read();
  bool lightVal = recieved == 1;
  if(lightVal)
  {
    digitalWrite(red, HIGH);
    digitalWrite(green, LOW);
  }
  else
  {
    digitalWrite(red, LOW);
    digitalWrite(green, HIGH);
  }
}
void crossroadOff()
{
  lcd.setCursor(3,1);
  lcd.print("Off");
  lcd.setCursor(1,3);
  lcd.write(4);
  lcd.setCursor(1,2);
  lcd.write(4);
  lcd.setCursor(1,1);
  lcd.write(4);

  lcd.setCursor(2,2);
  lcd.write(5);
  lcd.setCursor(3,2);
  lcd.write(5);
  lcd.setCursor(4,2);
  lcd.write(5);
  lcd.setCursor(5,2);
  lcd.write(5);
  lcd.setCursor(6,2);
  lcd.write(5);
}
void crossroadOn()
{
  lcd.setCursor(3,1);
  lcd.print("On");
  lcd.setCursor(1,3);
  lcd.write(4);
  lcd.setCursor(1,2);
  lcd.write(4);
  lcd.setCursor(2,2);
  lcd.write(4);
  lcd.setCursor(3,2);
  lcd.write(4);
  lcd.setCursor(4,2);
  lcd.write(4);
  lcd.setCursor(5,2);
  lcd.write(4);
  lcd.setCursor(6,2);
  lcd.write(4);

  lcd.setCursor(1,1);
  lcd.write(5);
  lcd.setCursor(5,1);
  lcd.write(5);
}

//Code to reference thats old
//Code to try and get data
/*  if(greenLine[12] == true)
  {
    lcd.print("good");
  }
  if(greenLine[150] == true)
  {
    lcd.print("wow");
  }
  lcd.print(greenLine[148]);
  lcd.print(greenLine[149]); */
/* while(Serial.available() == 0) {} 
  delay(1000);
  lcd.print(Serial.available());
  for(int i = 0; i < greenLineSize; i++)
  {
    char recieved = Serial.read();
    greenLine[i] = (recieved == '1');
  } */
