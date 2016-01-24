"""
A simple script for performing Pulse Width Modulation using the Raspberry Pi's 
GPIO pins.

The pins can provide enough current to blink one or several LEDs, connecting 
directly from a supported pin on the Pi, to the LED, and finally to the ground.
As the frequency becomes sufficiently high (or the duty cycle approachs 100), 
it becomes hard to see exactly when the LED is on or off.
So you can use that to create a "dimmer" for the LEDs, and other sorts of 
wacky things.
OK, at least in this short snippet, "dimming" a light is the wackiest thing 
you can do, but it's a start.
"""
import time
import RPi.GPIO as GPIO

FREQUENCY = 50

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, FREQUENCY) # pin, frequency in hertz

# Now for the demo
nsteps = 10 
stepsize = 100/nsteps
interval = 1.0

print("Frequency:", FREQUENCY, "Hz")

try:
    for i in range(nsteps + 1):
        duty = i*stepsize
        print("Duty Cycle:", duty)
        pwm.ChangeDutyCycle(duty)
        time.sleep(interval)
except KeyboardInterrupt:
    pass
finally:
    pwm.stop()
    GPIO.cleanup()