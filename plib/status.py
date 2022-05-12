#!/usr/bin/python3

# status.py    Basic Status (thread-safe)
#      import status provides printStatus(egpg,ds)
#      ./status.py    will print status once and exit
#
#      ./status.py -l (or -loop) will print status every 5 seconds
#
#      ./status.py -h (or --help) will print usage
#

# IMPORTS
import sys
import time
import signal
import os
from datetime import datetime
import argparse



# ######### CNTL-C #####
# Callback and setup to catch control-C and quit program

_funcToRun=None

def signal_handler(signal, frame):
  print('\n** Control-C Detected')
  if (_funcToRun != None):
     _funcToRun()
  sys.exit(0)     # raise SystemExit exception

# Setup the callback to catch control-C
def set_cntl_c_handler(toRun=None):
  global _funcToRun
  _funcToRun = toRun
  signal.signal(signal.SIGINT, signal_handler)

# Return CPU temperature as a character string
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=", "").replace("\n", ""))

# Return memory and swap
def getFree():
    res = os.popen('free -m').read()
    return res

# Return Clock Freq as a character string
def getClockFreq():
    res = os.popen('vcgencmd measure_clock arm').readline()
    res = int(res.split("=")[1])
    if (res < 1000000000):
        res = str(res/1000000)+" MHz"
    else:
        res = '{:.2f}'.format(res/1000000000.0)+" GHz"
    return res


# Return throttled flags as a character string
#   0x10001  under-voltage 4.63v occurred / occurring
#   0x20002  freq-cap occurred / occurring
#   0x40004  Temp Throttled occurred / occurring
#   0x80008  SOFT_TEMPERATURE_LIMIT (default 60degC, boot/config.txt temp_soft_limit=70 to increase)

def getThrottled():
    res = os.popen('vcgencmd get_throttled').readline()
    return res.replace("\n", "")


def getUptime():
    res = os.popen('uptime').readline()
    return res.replace("\n", "")

def printStatus():
    print("\n********* Pi4BE32 Basic STATUS ******")
    print("{} {}".format(datetime.now().date(), getUptime()))
    print("Processor Temp: %s" % getCPUtemperature())
    print("Clock Frequency: %s" % getClockFreq())
    print("%s" % getThrottled())
    print("Memory: ", getFree()[9:])

# ##### MAIN ######


def handle_ctlc():
    print("status.py: handle_ctlc() executed")


def main():
    # #### SET CNTL-C HANDLER
    set_cntl_c_handler(handle_ctlc)

    # ARGUMENT PARSER
    ap = argparse.ArgumentParser()
    ap.add_argument("-l", "--loop", default=False, action='store_true',
                    help="optional loop mode")

    args = vars(ap.parse_args())
    loopFlag = args['loop']

    try:
        while True:
                printStatus()
                if (loopFlag is False):
                    break
                else:
                    time.sleep(5)
        # end while
    except SystemExit:
        print("Exiting")


if __name__ == "__main__":
    main()
