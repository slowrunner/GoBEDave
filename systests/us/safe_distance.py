#!/usr/bin/env python3

from easygopigo3 import EasyGoPiGo3
from time import sleep



US_PORT = "AD2"

def test():
  try:
      if us.is_too_close() == True:
        print("US Sensor reports too close - {} mm".format(us.read_mm()))
  except Exception as e:
        print("Exception: {}".format(str(e)))

if __name__ == '__main__':
    egpg = EasyGoPiGo3(use_mutex=True)
    us = egpg.init_ultrasonic_sensor(US_PORT)

    print("US Default Safe Distance: {}".format(us.get_safe_distance()))
    us.set_safe_distance(127)  # 5 inches
    print("US Safe Distance Set To: {}".format(us.get_safe_distance()))


    while True:
        test()
        sleep(0.1)

