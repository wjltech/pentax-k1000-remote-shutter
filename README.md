# pentax-k1000-remote-shutter
Hi! Thanks for checking out this project.
The following is some info on what code files are for which part of this overall project in order.

**The following 2 files required IR_remote library to be installed within the Arduino IDE software environment** 

IR_Decode_Will
This code file is for the Arduino IDE software environment to be uploaded to an Arduino NANO in order to decode infrared signals and out put them as text
in the Serial Monitor Tool

IR_Control_Circuit_Arduino
This code file takes the infrared codes you saved from using IR_Decode_Will and tells the Arduino when receiving a code to output a Voltage on pin 9
It also tells the output to turn off if your using a button to turn the circuit off as well as on. See YouTube video for further clarification.

*The following file was loaded onto the Raspberry Pi PICO using software: Thonny*

shutter_release_V3
This runs a program on BOOT up of the the Raspberry Pi PICO that will output a Pulse Width Modulation signal from pin 20 (also known as GP15)
This PWM signal will run continiously on a loop and tells the small servo motor to:
wait 5 seconds
set position of servo to 180 °
wait 2 seconds
set position of servo to 0 °
wait 5 seconds 

Thanks for checking out the project!
