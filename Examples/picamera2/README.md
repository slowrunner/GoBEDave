<<<<<<< HEAD
# Using picamera2 with libcamera on PiOS Bullseye

1) Setup Picamera not to be legacy in raspi-config
2) install python3-libcamera and more
```
sudo apt install -y python3-libcamera python3-kms++

pip3 install v4l2-python3

cd
sudo pip3 install pyopengl piexif simplejpeg PiDNG
sudo apt install -y python3-pyqt5 python3-numpy python3-prctl ffmpeg
git clone https://github.com/raspberrypi/picamera2.git

Put the following at the end of /home/pi/.bashrc file:

export PYTHONPATH="${PYTHONPATH}:/home/pi/picamera2"

```
3) READ https://github.com/raspberrypi/picamera2/blob/main/README.md

=======
# Using picamera2 on Bullseye

REF:  https://github.com/raspberrypi/picamera2  


=== INSTALL ===  

- Do not enable Legacy Pi Camera in raspi-config  
```
sudo apt install -y python3-libcamera python3-kms++
sudo apt install -y python3-pyqt5 python3-prctl libatlas-base-dev ffmpeg
sudo pip3 install numpy --upgrade
sudo pip3 install picamera2
```

=== Examples ====

REF:  https://github.com/raspberrypi/picamera2/tree/main/examples

Examples requiring window server
```
capture_jpeg.py: Show preview and capture to ./test.jpg
wget https://raw.githubusercontent.com/raspberrypi/picamera2/main/examples/capture_jpeg.py
python3 capture_jpeg.py

opencv_face_detect.py: Show preview, loop capturing numpy array images for OpenCV face detector
wget https://raw.githubusercontent.com/raspberrypi/picamera2/main/examples/opencv_face_detect.py
python3 opencv_face_detect.py

opencv_face_detect_2.py: Demonstrates a low resolution stream feeding OpenCV Haar Cascade face detection
wget https://raw.githubusercontent.com/raspberrypi/picamera2/main/examples/opencv_face_detect_2.py
python3 opencv_face_detect_2.py

tensorflow/real_time_with_lables.py:  shows COCO object set recognition
cd tensorflow
./real_time_with_labels.py --model mobilenet_v2.tflite --label coco_labels.txt
or
./real_time.py --model mobilenet_v2.tflite --label coco_labels.txt
```

Examples w/o preview (no window server required):
```
capture_headless.py:  Capture a jpg image w/o preview (headless)
wget https://raw.githubusercontent.com/raspberrypi/picamera2/main/examples/capture_headless.py
python3 capture_headless.py

capture_video_h264.py:  Capture H264 video w/o preview
wget https://raw.githubusercontent.com/raspberrypi/picamera2/main/examples/capture_video.py
mv capture_video.py capture_video_h264.py
python3 capture_video_h264.py

capture_motion.py:  Record 2 second h264 video triggered by motion w/o preview window
wget https://raw.githubusercontent.com/raspberrypi/picamera2/main/examples/capture_motion.py
python3 capture_motion.py

snapJPG2.py:  Captures 320x240 image to ./image/<arg1> or   
              to ./images/capture_YYYYMMDD-HHMMSS.jpg if no arg1  
              (no preview)  
./snapJPG2.py


```
>>>>>>> 6c844246ba8c615dccd9b20c983bd0039b1ef583

