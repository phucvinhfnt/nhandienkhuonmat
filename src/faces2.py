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
    if name!="Unknown":
       
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

import face_recognition
import cv2
import numpy as np
video_capture = cv2.VideoCapture(0)

# Tải ảnh người cần nhận diện (đầu tiên là mình) va ma hoa anh do.
mau_image = face_recognition.load_image_file("E:/python/nhandienkhuonmat/src/sinh.jpg")
mau_face_encoding = face_recognition.face_encodings(mau_image)[0]


# vinh_image = face_recognition.load_image_file("phouvanh.jpg")
# vinh_face_encoding = face_recognition.face_encodings(vinh_image)[0]
#tHÊM 1 NGƯỜI = CÁCH

name_image = face_recognition.load_image_file("E:/python/nhandienkhuonmat/src/phucvinh.jpg")
name_face_encoding = face_recognition.face_encodings(name_image)[0]
uyen_image = face_recognition.load_image_file("E:/python/nhandienkhuonmat/src/minhuyen.jpg")
uyen_face_encoding = face_recognition.face_encodings(uyen_image)[0]

# Tạo 1 mang cac khuon mat da duoc ma hoa va ten
known_face_encodings = [
    mau_face_encoding,
    name_face_encoding,
    uyen_face_encoding,
]
known_face_names = [
    "LuongSinh",
     "Phuc Vinh",
     "Minh uyen",

]

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"
        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        excel(name)
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
cv2.destroyAllWindows()
