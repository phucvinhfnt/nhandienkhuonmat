from types import CellType
from typing import Text
import cv2
import numpy as np
import os
import pickle
import PIL as Image
# excellll---------------------------------------------
from datetime import date
import datetime
from tabnanny import check
import time
import xlwt
from xlwt import Workbook
import smtplib,ssl
import smtplib
from email.message import EmailMessage
import xlrd
from xlutils.copy import copy
def excel(name):
   
    ts = time.time()
    Date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    

    wbnew = xlrd.open_workbook('E:/python/nhandienkhuonmat/src/sample_data2.xls')
    sheet = wbnew.sheet_by_index(0)
    tamp = 0   
    check =0
    a=[]
    sheet.cell_value(0, 0)
    for row_num in range(sheet.nrows):
        row_value = sheet.cell_value(row_num,0)
        a.append(row_value)
    if name not in a:
        check =1
    if check==1:
        wb1 = copy(wbnew) 
        sheet = wb1.get_sheet(0) 
         #sheet1.write(row,col, data, style)
        sheet.write(row_num+1, 0,name)
        sheet.write(row_num+1, 1,Date)
        sheet.write(row_num+1, 2,Time)
        wb1.save('E:/python/nhandienkhuonmat/src/sample_data2.xls')    
    check=0

    
# =------------------------------------------------
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizers/face-trainner.yml")

def hienthidanhsach():
    	dd=3

		
label={"person_name": 1}
with open("pickles/face-labels.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}
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
		id_, conf= recognizer.predict(roi_gray)
		if conf>=0 and conf<=90                                                                                                                                                                                                                                                                                                                          :
			#print(id_)	
			font = cv2.FONT_HERSHEY_SIMPLEX
			name = labels[id_]
			excel(name)
			color = (255, 255, 255)
			stroke = 2
			dotincay=Text(round(conf,2))
			cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA) 
			cv2.putText(frame, dotincay, (x-100,y), font, 1, color, stroke, cv2.LINE_AA) 
		

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
print(label)
cap.release()
cv2.destroyAllWindows()		



	