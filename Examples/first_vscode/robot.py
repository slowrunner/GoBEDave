#!/usr/bin/python3

# FILE: robot1.py

# PURPOSE: Test import context sensitive help

from easygopigo3 import EasyGoPiGo3
import time

DIODE_DROP = 0.81

def main():
    egpg = EasyGoPiGo3(use_mutex=False)
    while True:
        try:
          vBatt = egpg.volt()
          print("\nrobot1.py:main(): Battery: {:.2f} volts".format(vBatt+DIODE_DROP))

          botInfo = egpg.get_version_hardware()
          print("robot1.py:main(): Hardware Version: {}".format(botInfo))

          time.sleep(1)
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()