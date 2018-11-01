# blur-detector
detects if the image contains blur
blur_detector.py
@Created on Thu Nov  1 15:29:59 2018

@author: Kiran
@Description: finds if the image contain blur or not
            it uses laplacian of the image, i.e focus measure of image
            based on threshold of the measure it categorizes blurry or not
@Usage: usage: blur_detector.py --images <valid image path> [-t threshold]
    uses threshold =100 by default if it is not supplied in the args

@Returns: 1 if the image contain blur
         0 if the image does not contain blur
@Credits: Pyimagesearch.com for tutorials and code
@pre-requesites: python 3.6.6 or python 2.7 opencv 3
        : tested it with anaconda and spyder
        : 
        :need below for opencv 3 with python
        pip install opencv-python
         pip install pathlib
        
        https://solarianprogrammer.com/2016/09/17/install-opencv-3-with-python-3-on-windows/
        https://www.scivision.co/install-opencv-python-windows/
