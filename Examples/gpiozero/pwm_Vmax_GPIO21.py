#!/usr/bin/env python3

# Stimulate GPIO21 to max voltage 
# Measure with with/without DC block to detect DC voltage and ripple
# C= .01 uF in series with red probe
# led.value=1.0 generates a 3.3V DC with ?v ripple
#

# REF: https://gpiozero.readthedocs.io/en/stable/recipes.html

from gpiozero import PWMLED
from time import sleep

led = PWMLED(21)

led.value = 1.0

while True:
        sleep(.1)

led.value = 0.0
