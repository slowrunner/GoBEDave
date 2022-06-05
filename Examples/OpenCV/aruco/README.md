# ArUco Markers


REF:  https://pyimagesearch.com/2020/12/21/detecting-aruco-markers-with-opencv-and-python/
REF ArUco Markers:  https://docs.google.com/document/d/1QU9KoBtjSM2kF6ITOjQ76xqL7H0TEtXriJX5kwi9Kgc/edit
REF Video on Bullseye: https://github.com/raspberrypi/picamera2
REF Generate ArUco Markers: https://fodi.github.io/arucosheetgen/

Requires:
- pip3 install imutils
- OpenCV
- picamera2 for aruco_video.py

```
./aruco_image.py --image images/ArUco_4x4.jpg --type DICT_4X4_50  
./aruco_image.py --image images/ArUco_6x6.jpg --type DICT_6X6_50  

./aruco_video.py --type DICT_4X4_50
./aruco_video.py --type DICT_6X6_50
```

On Pi4 2GB running Bullseye using picamera2 and OpenCV 4.5.5:  
aruco_video.py detects 2 markers in a frame in 20ms (~50  FPS)  
when "slowed" to a 10 FPS request, with a load average of 2.0  
and temperature of 50C in a PiMoroni Heat Sink Case.
