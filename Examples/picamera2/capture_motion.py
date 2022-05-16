#!/usr/bin/python3

# Modified to write motion files to ./captures/capture_YYYYMMDD-HHMMSS.h264

import time
from signal import pause
import os

import numpy as np
from datetime import datetime

from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput
from picamera2 import Picamera2

lsize = (320, 240)
picam2 = Picamera2()
video_config = picam2.video_configuration(main={"size": (1280, 720), "format": "RGB888"}, 
                                          lores={"size": lsize, "format": "YUV420"})
picam2.configure(video_config)
encoder = H264Encoder(1000000)
picam2.encoder = encoder
picam2.start()

w, h = lsize
prev = None 
encoding = False
ltime = 0

if not os.path.exists('captures'):
    os.makedirs('captures')

while True:
    cur = picam2.capture_buffer("lores")
    cur = cur[:w*h].reshape(h, w)
    if prev is not None:
        # Measure pixels differences between current and
        # previous frame
        mse = np.square(np.subtract(cur, prev)).mean()
        if mse > 7:
            if not encoding:
                # encoder.output = FileOutput("{}.h264".format(int(time.time())))
                fname = "captures/capture_"+datetime.now().strftime("%Y%m%d-%H%M%S")
                encoder.output = FileOutput("{}.h264".format(fname))
                picam2.start_encoder()
                encoding = True
                print("New Motion", mse)
            ltime = time.time()
        else:
            if encoding and time.time() - ltime > 2.0:
                picam2.stop_encoder()
                encoding = False
    prev = cur
