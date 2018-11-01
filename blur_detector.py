# -*- coding: utf-8 -*-
"""
blur_detector.py
Created on Thu Nov  1 15:29:59 2018

@author: Kiran
Description: finds if the image contain blur or not
            it uses laplacian of the image, i.e focus measure of image
            based on threshold of the measure it categorizes blurry or not
Usage: usage: blur_detector.py --images <valid image path> [-t threshold]
    uses threshold =100 by default if it is not supplied in the args

Returns: 1 if the image contain blur
         0 if the image does not contain blur
Credits: Pyimagesearch.com for tutorials and code
pre-requesites: python 3.6.6, opencv 3
        : tested it with anaconda and spyder
        : if testing with different distributions use below installations
        :go over below for opencv 3 with python
        https://solarianprogrammer.com/2016/09/17/install-opencv-3-with-python-3-on-windows/
        https://www.scivision.co/install-opencv-python-windows/
"""

# import the necessary packages
#argument parser
import argparse
#opencv 
import cv2
#file paths
from pathlib import Path
 
def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()

#the main function   
def main():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--images", required=True,
                    help="path to input directory of images")
    ap.add_argument("-t", "--threshold", type=float, default=100.0,
                    help="focus measures that fall below this value will be considered 'blurry'")
    args = vars(ap.parse_args())
    
    imagePath = args["images"]
    my_file = Path(imagePath)
    if my_file.is_file() and my_file.exists:
        # load the image, convert it to grayscale, and compute the
        # focus measure of the image using the Variance of Laplacian
        # method
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm = variance_of_laplacian(gray)
   
        # if the focus measure is less than the supplied threshold,
        # then the image should be considered "blurry"
        if fm < args["threshold"]:
            print(1)
            #print("blurry",fm, imagePath)
        else:
            print(0)
            #print("not blurry",fm, imagePath)
    else:
        print("usage: blur_detector.py --images <valid image path> [-t threshold]")

if __name__ == '__main__':
    main()