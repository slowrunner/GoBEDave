#!/usr/bin/env python3

# Stimulate GPIO21 with varying PWM

# REF: https://gpiozero.readthedocs.io/en/stable/recipes.html

from gpiozero import PWMLED
from signal import pause

led = PWMLED(21)

led.pulse()

pause()


