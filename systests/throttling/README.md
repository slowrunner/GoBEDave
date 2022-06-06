# Legacy PiOS DAVE Throttling Test

* GoPiGo3 v3.x.x
* 11.1v nominal Li-Ion Battery

* Running stress -c 3 -t 300 just bumps the 60degC soft temp limit  
  (which does not trigger temperature throttling)
* Running stress -c 4 -t 300 will reach 68degC, but will not trigger throttling

Note: No under_voltage throttling occured in either test  
      Battery indicated 8W draw at 11.1v

Running processes:
- throttling.sh

```
#!/bin/bash  
#  
# loop printing out processor temp, processor clock freq, and throttled status  
#  
# 0x50000  means throttling occurred, under-voltage occurred  
# 0x50005  means throttled now and under-voltage now  
# 0x80008  means soft temperature limit exceeded (no throttling yet)  
#  
while true; do uptime && vcgencmd measure_temp && vcgencmd measure_clock arm && vcgencmd get_throttled; free -t -m; sleep 2; echo ''; done  
```

- stress -c 4 -t 300
```
pi@PIOSLGCY:~/GoPiLgc/systests/throttling $ stress -c 4 -t 300
stress: info: [4296] dispatching hogs: 4 cpu, 0 io, 0 vm, 0 hdd
stress: info: [4296] successful run completed in 300s
```

- gopigo3_power.py
- loglife.py
- safetyShutdown.py
- wheelLog.py



```
temp=67.7'C
frequency(48)=1200000000
throttled=0x80008
              total        used        free      shared  buff/cache   available
Mem:            871         171         401          14         298         629
Swap:            99           0          99
Total:          971         171         501

 13:41:15 up 15 min,  2 users,  load average: 4.05, 3.33, 1.81
```

