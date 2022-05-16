# TensorFlow-Lite using picamera2 with OpenCV 4.5.5 on Bullseye32 

Installed:
- OpenCV 4.5.5 from sources
- picamera2

Modified to output integer x,y and 0.xxx scores

```
python3 real_time_with_labels.py --model mobilenet_v2.tflite --label coco_labels.txt

or 

python3 real_time.py --model mobilenet_v2.tflite --label coco_labels.txt
...
