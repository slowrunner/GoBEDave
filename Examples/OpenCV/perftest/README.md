# BASIC OpenCV PERF TEST

test1.py: 
- Measures the OpenCV Hough Probabalistic Lines Transform  
  applied to the test image using  
  - CodeTimer for 1 execution  
  - datetime on 10 executions  

Pi4B 2GB - OpenCV 4.5.5 - Python3.9:     306ms 3.3 FPS  
(built from sources, load 0.08 )  
 
Pi3B 1GB - OpenCV 4.1.1 - Python3.7.3:   686ms 1.4 FPS  
(pip3 install opencv-contrib-python, load 0.36 w/Carl processes running)  

