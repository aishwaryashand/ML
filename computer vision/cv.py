#!/usr/bin/python3

import cv2

# loading image 
img=cv2.imread('Dog.jpg',0)

# print height and width
print("shape is: ",img.shape)

# to display that image
cv2.imshow("Dog",img)

# image window holder activate
cv2.waitKey(0)

# wait key will destroy by using q button
cv2.destroyAllWindows()
