#!/usr/bin/python3

import cv2
import time

# reading image
img=cv2.imread('Dog1.jpeg')

# checking shape
#print (img.shape)
time.sleep(5)

# printing data
#print (img)

# extracting only red color
onlyred=cv2.inRange(img,(0,0,0),(40,40,255))
cv2.imshow('original image',img)
cv2.imshow('onlyred',onlyred)
cv2.waitKey(0)
cv2.destroyAllWindows()

