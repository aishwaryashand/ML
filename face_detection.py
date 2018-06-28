#!/usr/bin/python3

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
cap=cv2.VideoCapture(0)
while True:
	status,frame=cap.read()
	grayimg=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(grayimg,1.15,5)
	for (x,y,w,h) in  faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
		roi_gray=grayimg[y:y+h,x:x+w]
		roi_color=frame[y:y+h,x:x+w]
	# showing current image
	cv2.imshow("current image",frame)
	if cv2.waitKey (1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()
cap.release()
