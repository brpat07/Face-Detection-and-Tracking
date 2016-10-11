//header...call function library
#include <Servo.h> 

Servo servo;

// User input for servo and position
int UserIn[3];    // raw input from serial buffer, 3 bytes
int ini_byt;       // start byte, begin reading input//initial byte
int servo_num;           // which servo to pulse?
int pos;             // servo angle 0-180
int i;               // iterator
int t=90;    //variable to move to according angle


// Common servo setup values
int mini_Pul = 600;   // minimum servo position, us (microseconds)
int maxi_Pul = 2400;  // maximum servo position, us



void setup() 
{   
  servo.attach(9, mini_Pul, maxi_Pul); // Attach each Servo object to a digital pin
  Serial.begin(9600); // Open the serial connection, 9600 baud
} 



void loop() 
{ 
  if (Serial.available() > 2) // Wait for serial input (min 3 bytes in buffer)
    {
      ini_byt = Serial.read();// Read the first byte
      if (ini_byt == 255) // If it's really the startbyte (255) ...
         {
          for (i=0;i<2;i++) // ... then get the next two bytes
              {
                UserIn[i] = Serial.read();
              }
          servo_num = UserIn[0];// First byte = servo to move?          
          pos = UserIn[1];// Second byte = which position?          
          if (pos == 255) // Packet error checking and recovery
              { 
                servo_num = 255; 
              }
          if (pos==1)
            {
              t=t+3;
              servo.write(t); 
            }
         else if (pos==2)
           {
             t=t-3;
             servo.write(t);
         
           }  
         }
    }
}
