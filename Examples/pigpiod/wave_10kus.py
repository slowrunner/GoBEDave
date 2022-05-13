#!/usr/bin/env python

import time
import pigpio

pi = pigpio.pi()
if not pi.connected:
   exit()

gpios = [21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]

pulses = [
   (0x200000, 0x200000, 10000), 
   (0x200000, 0x200000, 10000), 
   (0x200000, 0x200000, 10000), 
   (0x200000, 0x200000, 10000), 
   (0x200000, 0x200000, 10000), 
   (0x200000, 0x200000, 10000), 
   (0x200000, 0x200000, 10000), 
   (0x200000, 0x200000, 10000), 
]

for g in gpios:
   pi.set_mode(g, pigpio.OUTPUT)

wf = []
for p in pulses:
   wf.append(pigpio.pulse(p[0], p[1], p[2]))

pi.wave_clear()
pi.wave_add_generic(wf)

wid = pi.wave_create()
if wid >= 0:
   pi.wave_send_repeat(wid)
   time.sleep(30)
   pi.wave_tx_stop()
   pi.wave_delete(wid)

pi.stop()

