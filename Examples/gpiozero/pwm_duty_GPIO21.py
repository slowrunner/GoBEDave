#!/usr/bin/env python3

# Stimulate GPIO21 with set duty cycle
# Measure with with/without DC block to detect DC voltage and ripple
# C= .01 uF in series with red probe
# led.value=1.0 generates a 100% duty cycle or constant 3.3V DC
#

# REF: https://gpiozero.readthedocs.io/en/stable/recipes.html

from gpiozero import PWMLED
from time import sleep

led = PWMLED(21)

# Set duty cycle
led.value = 0.50

try:
    while True:
        sleep(.1)
except KeyboardInterrupt:
    pass

led.value = 0.0
sleep(.1)
