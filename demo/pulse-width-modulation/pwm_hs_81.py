"""
A quick script for testing out the HS-81 servo, controlled by pulse-width
modulation using the Raspberry Pi's GPIO pins.

Writeup
=======

In general, the procedure seems to be:
    1.  Find out the frequency that controls the servos
    2.  Choose a good frequency for the PWM (sometimes it is suggested by the
        frequency refresh rate of the servo)
    3.  Determine how much of a duty cycle you need for "full left" and 
        "full right" on the servos in question.

Here, the HS-81 expects a pulse width between 900-2100 microseconds, and it has
a frequency refresh of 50Hz, or once every 20ms.
So we set the frequency of the Raspberry Pi's PWM to 50 Hz.
To get a pulse lasting 900us, we need a duty cycle of about 4.5, since 4.5
percent of 20 is 0.9, and for a pulse lasting 2100us, we need a duty cycle of
10.5 (following similar reasoning). 

Troubleshooting
---------------

The servo may act "jerky" moving to the correct place and then twitching a bit.
This is apparently due to issues with the amount of power available.
It is especially an issue if you're running the servo off of the Pi's power
supply.
Apparently it can be remedied by including a capacitor in the power circuit;
electronics people on the Internet suggest ~500uF or greater.
"""
import time
import RPi.GPIO as GPIO

FREQUENCY = 50
MIN_DUTY = 4.5
MAX_DUTY = 10.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, FREQUENCY) # pin, frequency in hertz

# Now for the demo
nsteps = 10 
stepsize = (MAX_DUTY - MIN_DUTY)/nsteps

try:
    for i in range(nsteps + 1):
        duty = i*stepsize + MIN_DUTY
        print("Duty Cycle:", duty)
        pwm.ChangeDutyCycle(duty)
except KeyboardInterrupt:
    pass
finally:
    pwm.stop()
    GPIO.cleanup()