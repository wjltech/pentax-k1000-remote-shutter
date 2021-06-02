from machine import Pin, PWM
import utime

# On-time of servo motor. 3 defined objects.

MIN = 1000000 #this is 1 millisecond. motor will be in 0°
MID = 1500000 #this is 1.5 milliseconds. motor will be an 90°
MAX = 2000000 #this is 2 milliseconds. moteo will be at 180°

led = Pin(25,Pin.OUT) #turn on onboard LED
pwm = PWM(Pin(15)) #output pwm signal to servo
pwm.freq(50) #frequency of pwm signal
pwm.duty_ns(MID) #set pulse width of pwm signal to MID object. 1.5 milliseconds

while True: #this statement creates an infinite loop
        utime.sleep(2) #waits 5 seconds
        pwm.duty_ns(MAX) #turns servo motor to 180°
        utime.sleep(2) #waits 2 seconds
        pwm.duty_ns(MIN) #turns servo motor to 0°
        utime.sleep(5) #waits 5 seconds
        