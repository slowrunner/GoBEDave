#!/usr/bin/env python3

from easygopigo3 import EasyGoPiGo3
from time import sleep



US_PORT = "AD2"

def test(sensor):
    print("US Sensor in AD2 reports {} mm".format(us.read_mm()),end="\r", flush=True)

if __name__ == '__main__':
    egpg = EasyGoPiGo3(use_mutex=True)
    us = egpg.init_ultrasonic_sensor(US_PORT)
    print("\nCntrl-C to quit test")
    print("Ignore any initial get_grove_value error")
    us.read_mm()  # flush a possible bad value error
    print("\n")

    while True:
        try:
            test(us)
            sleep(0.1)
        except KeyboardInterrupt:
            print("\nCtrl-c Detected.  Exiting")
            exit()

