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


