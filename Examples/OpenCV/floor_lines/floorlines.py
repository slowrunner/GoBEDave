#!/usr/bin/env python3

"""
@file floorlines.py
@brief This program demonstrates finding lines in the floor in front of robot
"""

import sys
import math
import cv2 as cv
import numpy as np
from datetime import datetime

def display(windowname, image, scale_percent=30):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    imagesmall = cv.resize(image, dim, interpolation = cv.INTER_AREA)
    cv.imshow(windowname, imagesmall)

def halfscrn_scale(image):
    halfscreen = 612
    scale = int(halfscreen/image.shape[1] * 100)
    return scale

# from http://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/
def find_l_h_thresh(gray_image):
    v = np.median(gray_image)
    sigma = 0.33  # sigma around median value
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    lower = 15
    upper = 25
    return lower, upper

def region_of_interest(image):
    # return an image masked to triangular region of interest
    # Masked off left and right 15% at bottom
    # Peak of triangular region of interest is 40% from bottom
    # print("input image.shape:",image.shape)
    height = image.shape[0]
    width  = image.shape[1]
    bottom_of_frame = height
    left_limit = int(0.15 * width)
    right_limit = int(0.85 * width)
    ctr = int(width * 0.5)  # originally 550 or 43%, slightly off to left
    horizon = int(height * 0.60) # originally 250 or 35% down from top
    triangle = np.array([(left_limit, bottom_of_frame), (right_limit, bottom_of_frame),(ctr, horizon)])
    polygons = np.array([ triangle ])  # only one polygon in the polygons array
    mask = np.zeros_like(image)
    cv.fillPoly(mask, polygons, 255)
    masked_image = cv.bitwise_and(image, mask)
    return masked_image

def select_best_line(lines,w,h):
        # lines: array of lines [[x0 y0 x1 y1]]
        # w: image width
        # h: image height
        print("select_best_line: image w: {}  h: {}".format(w,h))
        print("select_best_line: Analysing {} Lines".format(len(lines)))
        ratings = []
        distances = []
        angles = []
        best_line = None
        # optimal x and y
        ox = int(w/2)
        oy = h
        for i in range(0, len(lines)):
            l = lines[i][0]
            dx0 = ox-l[0]
            dy0 = oy-l[1]
            dy  = l[0]-l[2]
            dx  = l[1]-l[3]
            angle = int(math.atan2(dy,dx) * 180.0 / math.pi)
            dist = int(math.sqrt(dx0 ** 2 + dy0 ** 2))
            distances += [dist]
            angles += [angle]
            print("Line[{}]: [{}, {}], [{}, {}] angle: {} dist: {}".format(i, l[0], l[1], l[2], l[3], angle, dist))
            ratings += [dist]

        print("distances:",distances)
        print("angles:",angles)

        best_rating = min(ratings)
        print("best_rating:",best_rating)

        best_line_idx = ratings.index(best_rating)
        print("best_line_index", best_line_idx)

        best_line = lines[best_line_idx][0]
        print("best_line:", best_line)

        l=best_line
        i=best_line_idx
        print("best line {}: [{}, {}], [{}, {}] rating: {}".format(i, l[0], l[1], l[2], l[3], best_rating))

        return best_line

def main(argv):

    default_file = 'images/floor.jpg'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    try:
        src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_GRAYSCALE)
    except:
        print ('Error opening image!')
        print ('Usage: hough_lines.py [image_name -- default ' + default_file + '] \n')
        return -1

    start = datetime.now()

    # Convert source image  to grayscale
    gsrc = cv.cvtColor(src, cv.COLOR_GRAY2BGR)

    # Mask to region of interest

    mgsrc = region_of_interest(gsrc)

    # Blur region of interest
    mgbsrc = cv.GaussianBlur(mgsrc, (5,5), 0)

    # Find lower and upper thresholds for canny
    lower, upper = find_l_h_thresh(mgbsrc)

    # Find edges in image
    # - image (8-bit)
    # - threshold1 for hysteresis procedure
    # - threshold2 for hysteresis procedure
    # - aperatureSize for Sobel operator
    # - L2gradiant flag (False: Normal,  True:more accurate)
    # dst = cv.Canny(src, 50, 200, None, 3)
    cmgbsrc = cv.Canny(mgbsrc, lower, upper)

    # Convert canny result to grayscale
    # cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)

    # Get lines on the canny image using Probabilistic Hough Transform
    # - Input Array
    # - Output Array of lines
    # - rho: Distance resolution of the accumulator in pixels
    # - theta:  Angle resolution of the accumulator in radians
    # - threshold: Only return lines with enough votes
    # - minLineLength=0
    # - maxLineGap=0

    # linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)

    # best for 1092x819 undocked
    # linesP = cv.HoughLinesP(cmgbsrc, 1, np.pi / 180, 50, None, 50, 100)

    # best for 320x240 undocked
    # linesP = cv.HoughLinesP(cmgbsrc, 1, np.pi / 180, 25, None, 40, 40)

    # best for 320x240 near
    linesP = cv.HoughLinesP(cmgbsrc, 1, np.pi / 180, 25, None, 20, 40)

    # select best line to follow
    bestLine = select_best_line(linesP, src.shape[1], src.shape[0])

    end = datetime.now()
    time_taken = (end - start)
    print("Execution time {}  for {:.1f} FPS".format(time_taken, 1.0/time_taken.total_seconds() ))

    red = (255, 0, 0)
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            # print("Line[{}]: [{}, {}], [{}, {}]".format(i, l[0], l[1], l[2], l[3]))
            # Draw lines on canny image
            # cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)
            cv.line(cmgbsrc, (l[0], l[1]), (l[2], l[3]), red, 1, cv.LINE_AA)
            # cv.line(src, (l[0], l[1]), (l[2], l[3]), red, 3)
        if (len(bestLine) > 0):
            # bestLine = bestLine[0]
            cv.line(src, (bestLine[0], bestLine[1]), (bestLine[2], bestLine[3]), red, 1)
    try:
        # cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
        # display("Detected Lines (in red) - Standard Hough Line Transform", cdst, scale_percent=30)
        # cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)
        scale = halfscrn_scale(cmgbsrc)
        display("Detected Lines (red) - Probabilistic Line Transform", cmgbsrc, scale_percent=scale)

        # cv.imshow("Source", src)
        scale = halfscrn_scale(src)
        display("Source", src, scale_percent=scale)

        cv.waitKey()
    except Exception as e:
        print("Exception: {}".format(str(e)))
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])
