#!/bin/bash

echo "Routine Shutdown Requested"
/home/pi/GoBEDave/logMaintenance.py "Routine Shutdown"
batt=`(/home/pi/GoBEDave/plib/battery.py)`
/home/pi/GoBEDave/logMaintenance.py "'$batt'"
sudo shutdown -h +2
