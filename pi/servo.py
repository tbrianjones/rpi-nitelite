from RPIO import PWM
import time as time

servo = PWM.Servo()
servo.set_servo( 17, 1200 )
time.sleep( 3 )