from types import CellType
from typing import Text
import cv2
import numpy as np
import os
import pickle
import PIL as Image
# excellll---------------------------------------------

# =------------------------------------------------
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()


def hienthidanhsach():
    	dd=3

		

cap= cv2.VideoCapture(0)
while(True):
    	#capture frame by frame 
	ret,frame=cap.read()
	#chuyen sang xam
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	ret,frame=cap.read()
	faces= face_cascade.detectMultiScale(gray, 1.2, 5)
	
	for(x,y,w,h)in faces:
		#print(x,y,w,h)#ROI- region of interest - vung` quan tam`
		roi_gray=gray[y:y+h,x:x+w]#crop mat trong anh
		roi_color=frame[y:y+h,x:x+w]
		#  deep learned model predict keras tensorflow pytorch scikit learn
		

		img_item="4.png"
		cv2.imwrite(img_item,roi_color)

		color= (255,0,0)#blue
		stroke=2
		end_cord_x=x+w
		end_cord_y=y+h
		cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y),color,stroke)#tao khung
	cv2.imshow('frame',frame)
	if cv2.waitKey(20)&0xFF==ord('q'):
    		break

cap.release()
cv2.destroyAllWindows()		



	