#!/usr/bin/env python3

import RPi.GPIO
import time

GPIO = 21
FREQ = 1185  # to get 1000Hz
DUTYCYCLE = 50 # percent

def square_wave(freq,gpio):
    RPi.GPIO.setwarnings(False)
    RPi.GPIO.setmode(RPi.GPIO.BCM)
    RPi.GPIO.setup(gpio, RPi.GPIO.OUT)
    try:
        p = RPi.GPIO.PWM(gpio, freq)
        p.start(DUTYCYCLE)
        while True:  # square wave loop
            time.sleep(1)
    except KeyboardInterrupt:
        p.stop

if __name__ == '__main__':
    square_wave(FREQ, GPIO)
