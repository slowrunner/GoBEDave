#!/usr/bin/env python

import time

import pigpio
import sys

usage = "Usage:  squarewave.py <hz> <GPIOnn>"
argc = len(sys.argv)

if argc < 3:
   print(usage)
   exit()

FREQ = int(sys.argv[1])

if (100000 < FREQ < 1):
    print("Frequency must be between 1 and 100000")
    exit()

GPIO=int(sys.argv[2])

if (26 < GPIO < 1):
    print("GPIO Num must be between 1 and 26")
    exit()

square = []

# Compute period
microsec = int(1000000/FREQ)

# Compute On time / Off time for 50% duty cycle
microsec = int(microsec/2)
#                          ON       OFF    MICROS
square.append(pigpio.pulse(1<<GPIO, 0,       microsec))
square.append(pigpio.pulse(0,       1<<GPIO, microsec))

pi = pigpio.pi() # connect to local Pi

pi.set_mode(GPIO, pigpio.OUTPUT)

pi.wave_add_generic(square)

wid = pi.wave_create()
try:
    if wid >= 0:
       pi.wave_send_repeat(wid)
       time.sleep(60)
       pi.wave_tx_stop()
       pi.wave_delete(wid)
except KeyboardInterrupt:
    if wid >= 0:
       pi.wave_tx_stop()
       pi.wave_delete(wid)


pi.stop()
