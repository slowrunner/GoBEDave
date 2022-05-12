#!/usr/bin/env python3

# Stimulate GPIO21 with varying PWM

# REF: https://gpiozero.readthedocs.io/en/stable/recipes.html

from gpiozero import PWMLED
from time import sleep

led = PWMLED(21)


while True:
    for i in range(0,100,10):
        led.value = i/100.0
        sleep(.01)
    for i in range(100,0,-10):
        led.value = i/100.0
        sleep(.01)
