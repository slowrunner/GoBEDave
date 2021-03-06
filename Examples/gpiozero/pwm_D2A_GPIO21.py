#!/usr/bin/env python3

# Stimulate GPIO21 with with/without DC block to detect DC voltage and ripple
# C= .01 uF in series with red probe
# 0.5 generates a 1.65V average with ?v ripple
# 0.2 generates about 677-mV DC with ?V indicated ripple
#

# REF: https://gpiozero.readthedocs.io/en/stable/recipes.html

from gpiozero import PWMLED
from time import sleep

led = PWMLED(21)

led.value = 0.3
try:
    while True:
        sleep(.1)
except KeyboardInterrupt:
    pass

led.value = 0.0
sleep(.1)
