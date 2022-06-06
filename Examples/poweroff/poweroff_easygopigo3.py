#!/usr/bin/env python3



#   FILE:  poweroff_easygopigo3.py

#   PURPOSE: Test current/power difference of issuing a set_motor_power(-128)
#            to totally remove power flowing to motors


from time import sleep
from easygopigo3 import EasyGoPiGo3

# imports for test main
import sys
sys.path.append("/home/pi/GoPiLgc/plib")
import speak


class My_EasyGoPiGo3(EasyGoPiGo3):

    def __init__(self, config_file_path="/home/pi/Dexter/gpg3_config.json", use_mutex=True):
        super().__init__(config_file_path=config_file_path, use_mutex=use_mutex)

    def stop_with_power_off(self):
        self.set_motor_dps(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)
        sleep(0.25)
        self.set_motor_power(self.MOTOR_LEFT + self.MOTOR_RIGHT, self.MOTOR_FLOAT)





def main():  # TEST
    megpg = My_EasyGoPiGo3()

    stmt="GO PI GO 3 POWER-OFF TEST"
    print(stmt)
    speak.whisper(stmt,anytime=True)

    stmt="SLEEPING FOR 1 MINUTE TO SETTLE LOAD"
    print(stmt)
    speak.whisper(stmt,anytime=True)
    sleep(60)

    stmt="BEFORE ANY DRIVE COMMANDS"
    print(stmt)
    speak.whisper(stmt,anytime=True)

    stmt="Please record current and power now"
    print(stmt)
    speak.whisper(stmt,anytime=True)

    stmt="SLEEPING FOR 5 MINUTES"
    print(stmt)
    speak.whisper(stmt,anytime=True)
    sleep(300)

    stmt="Please record current and power now"
    print(stmt)
    speak.whisper(stmt,anytime=True)


    # First use motors to have them
    stmt="CAUTION, ABOUT TO MOVE FORWARD WITH drive_cm(10)"
    print(stmt)
    speak.whisper(stmt,anytime=True)
    sleep(5)
    megpg.drive_cm(10)

    stmt="Please record current and power now"
    print(stmt)
    speak.whisper(stmt,anytime=True)

    stmt="SLEEPING FOR 5 MINUTES"
    print(stmt)
    speak.whisper(stmt,anytime=True)
    sleep(300)

    stmt="Please record current and power now"
    print(stmt)
    speak.whisper(stmt,anytime=True)

    stmt="SENDING POWER-OFF TO MOTORS"
    print(stmt)
    speak.whisper(stmt,anytime=True)
    megpg.stop_with_power_off()

    stmt="Please record current and power now"
    print(stmt)
    speak.whisper(stmt,anytime=True)

    stmt="SLEEPING FOR 5 MINUTES"
    print(stmt)
    speak.whisper(stmt,anytime=True)
    sleep(300)

    stmt="Please record current and power now"
    print(stmt)
    speak.whisper(stmt,anytime=True)


    # Now use motors with forward command 
    stmt="CAUTION, ABOUT TO MOVE for 1 second with forward() command"
    print(stmt)
    speak.whisper(stmt,anytime=True)
    sleep(5)

    megpg.forward()
    sleep(1)
    megpg.stop()

    stmt="Please record current and power now"
    print(stmt)
    speak.whisper(stmt,anytime=True)

    stmt="SLEEPING FOR 5 MINUTES"
    print(stmt)
    speak.whisper(stmt,anytime=True)
    sleep(300)

    stmt="Please record current and power now"
    print(stmt)
    speak.whisper(stmt,anytime=True)

    stmt="SENDING POWER-OFF TO MOTORS"
    print(stmt)
    speak.whisper(stmt,anytime=True)
    megpg.stop_with_power_off()

    stmt="Please record current and power now"
    print(stmt)
    speak.whisper(stmt,anytime=True)

    stmt="SLEEPING FOR 5 MINUTES"
    print(stmt)
    speak.whisper(stmt,anytime=True)
    sleep(300)

    stmt="Please record current and power now"
    print(stmt)
    speak.whisper(stmt,anytime=True)



    stmt="TEST COMPLETE"
    print("***",stmt,"***")
    speak.whisper(stmt,anytime=True)


if __name__ == "__main__": main()
