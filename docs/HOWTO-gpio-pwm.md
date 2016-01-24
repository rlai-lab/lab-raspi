# Pulse-Width Modulation

Pulse width modulation (PWM) is just sending a square wave of varying duration along a wire.
One way to perform it is via setting a *frequency* and a *duty cycle*.
By setting the frequency, you split time into discrete intervals.
The duty cycle determines the amount of time during the interval that the pulse is at a high voltage.
A duty cycle of zero means "never high", while a duty cycle of 1.0 (or 100%) means that the voltage is "always high".

For values in between 0 and 100, the pulse will start high, spend that percentage of the interval in that state, before dropping to zero for the rest of the interval. 
This process repeats constantly while PWM is happening.

Although in theory it would be just as reasonable to specify an amount of time to be active and inactive, most of the time you're performing PWM to control some sort of device that expects you to stick to a set frequency and only vary the duty cycle.

## PWM on the Raspberry Pi

The Raspberry Pi has a number of pins which support PWM, as well as a number of libraries for performing it via the programming language of your choice.

A number of people have tested how well the Raspi can perform modulation, but those benchmarks can be somewhat deceiving.
Depending on the code that's running in the background, you may end up with significantly degraded performance.
Additionally, since the PWM is implemented in userspace[^userspace-pwm], your beautiful square waves may get preempted by the kernel or other processes at various points in time.

You can reliably power an LED via just the PWM pin on the Raspberry Pi, and I have been able to run a single servo via Pi's power supply pins while controlling it via PWM in software, but this may not be ideal.
Your servo (or whatever else) may need more power, or more consistent power, and to get really rock-steady performance you might need to get a separate board/chip to perform PWM.

# PWM Code

A simple script to perform pulse-width modulation, for example with an LED circuit between pins `BCM 18` and `GROUND`.
[Consult a pinout diagram if you're uncertain](https://www.pinout.xyz)

```python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 50) # pin, frequency in hertz
pwm.start(5) # duty cycle, between 0.0 and 100.0

try:
    while True:
        pass
except KeyboardInterrupt:
    pass
finally:
    pwm.stop()
    GPIO.cleanup()
```

The frequency can be changed via 

```python
pwm.ChangeFrequency(__new_frequency)
```

And the duty cycle can be changed either through `pwm.start()` or via 

```python
pwm.ChangeDutyCycle(__new_duty_cyycle)
```

# Sources

http://razzpisampler.oreilly.com/ch05.html

http://pinout.xyz

[^userspace-pwm]: At least, I think it is, but consult your distro's documentation to be sure.