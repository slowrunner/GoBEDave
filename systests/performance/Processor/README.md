# Pi4 Processor Performance

Tested Pi4 with PiOS Bullseye 32-bit  
Pimoroni HeatSinkCase (Green)  

- stress --cpu 3  
- htop  
- plib/status.py  
- vnc


Load average 3.03  
Processor Temp: 59.9C  
Clock Freq: 1.8 GHz  
throttled=0x0  
Power: 4W 0.77A at 5.17v  
       idle: 1.6W 0.35A at 5.21v  
   

Tested Pi4 with PiOS Bullseye 32-bit  
Pi4 chip Heatsinks and in GoPiGo3

- htop  
- plib/status.py  
- vnc

Before Test:  
Load average: .11  
Temp: 45C  
Clock 700MHz to 1GHz  
Power: 5.6W 9.5V at 0.6A  

Adding (results at 8 minutes): 
- stress --cpu 3  

Load average: 3.11  
Memory Used: 228MB
Processor Temp: 75C  
Clock 1.8GHz  
Throttled=0x0  
Power: 7.9W 9.0V at 0.89A  

OS: 5.15.32-v7l+  Mar 31 2022 Bullseye 32-bit
