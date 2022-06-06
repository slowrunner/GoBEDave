#!/usr/bin/env python3

from easygopigo3 import EasyGoPiGo3
from time import sleep



US_PORT = "AD2"

def my_too_close(sensor, safe_mm=500):
    try:
        return (sensor.read_mm() < safe_mm)
    except Exception as e:
        print("Exception:", str(e))
        return True


def test(sensor):
  if my_too_close(sensor,127) == True:
    print("US Sensor reports too close - {} mm".format(us.read_mm()))

if __name__ == '__main__':
    egpg = EasyGoPiGo3(use_mutex=True)
    us = egpg.init_ultrasonic_sensor(US_PORT)

    while True:
        test(us)


