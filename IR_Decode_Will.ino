#include <IRremote.h> //including infrared remote header file

const int RECV_PIN=7;    //create a receiver on pin number 7
IRrecv irrecv(RECV_PIN);
decode_results results;


void setup()
{
Serial.begin(9600);
irrecv.enableIRIn();
}
void loop() {

if (irrecv.decode(&results))// Returns 0 if no data ready, 1 if data ready.
{
  switch(results.value){
  }

int readResults = results.value;// Results of decoding are stored in result.value
Serial.println(" ");
Serial.print("Code: ");
Serial.println(results.value); //prints the value a a button press
Serial.println(" ");
irrecv.resume(); // Restart the ISR state machine and Receive the next value
}
}
