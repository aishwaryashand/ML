#!/usr/bin/python3

import cv2
import random

# now starting web cam
cap=cv2.VideoCapture(0)
while cap.isOpened():
	print ("Camera is working, be ready to be clicked.")
	# current camera data after camera take frame status
	status,frame=cap.read()

	#for black n white image
	bwing=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	# adding a rectangle to your image
	cv2.rectangle(frame,(100,100),(400,350),(0,0,255),5)
	font=cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(frame,"Hello Dear",(100,100),font,2,(255,0,0))

	# shows image
	cv2.imshow("camera1",frame)
	cv2.imshow("camera2",bwing)

	#to save images by different names
	x=random.random()
	y=str(x)[2:6]
	cv2.imwrite('warya'+y+'.jpeg',frame)
	cv2.imwrite('warya'+y+'.jpeg',bwing)

	# keyboard instruction to close camera
	# waitKey is window holder activate
	if cv2.waitKey(1) & 0xFF==ord('q'):
	 break

# waitKey will destroy by using q button
cv2.destroyAllWindows()
cap.release()
