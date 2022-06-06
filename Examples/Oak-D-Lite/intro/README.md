# GoPiLgc Oak-D-Lite Introduction

Ref: https://learnopencv.com/introduction-to-opencv-ai-kit-and-depthai  
Ref: https://docs.luxonis.com/projects/api/en/latest/install/  

Oak-D-Lite Features/Specs
- RGB Camera: 12 MPx, 4k, up to 60 fps
- Mono Camera: 640x480p, 120 fps, Global Shutter
- No IMU
- Power/Interface: USB-C
- VPU:  Intel Myriad-X, 4 trillion ops/s

INITIAL INSTALL
```
cd ~/GoPiLgc/Examples/Oak-D-Lite/intro
git clone https://github.com/luxonis/depthai.git
cd depthai
sudo curl -fL https://docs.luxonis.com/install_dependencies.sh | bash
python3 install_requirements.py 
  - installs opencv-python 4.4, opencv_contrib_python 4.4, depthai 2.13 
  - installs all to /home/pi/.local/bin
python3 depthai_demo.py
cd ~/GoPiLgc
nano .gitignore
#IGNORES
Examples/Oak-D-Lite/intro/depthai/
```

