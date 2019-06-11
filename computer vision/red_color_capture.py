#!/usr/bin/python3

import cv2

# reading image
cap=cv2.VideoCapture(0)
while cap.isOpened():
	# taking frames
	status,frame=cap.read()
	# extracting red color
	onlyred=cv2.inRange(frame,(0,0,0),(255,40,40))
	cv2.imshow('only red',onlyred)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()
cap.release()
