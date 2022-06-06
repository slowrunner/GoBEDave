#!/usr/bin/python3

# FILE: robot1.py

# PURPOSE: Test import context sensitive help

from easygopigo3 import EasyGoPiGo3
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(funcName)s: %(message)s')

DIODE_DROP = 0.81

def main():
    egpg = EasyGoPiGo3(use_mutex=True)
    botInfo = egpg.get_version_hardware()
    print("Hardware Version: {}".format(botInfo))

    while True:
        try:
            vBatt = egpg.volt()
            logging.info("Battery: {:.2f} volts".format(vBatt+DIODE_DROP))
            time.sleep(1)

        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()