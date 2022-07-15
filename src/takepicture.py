from types import CellType
from typing import Text
from unicodedata import name
import cv2
import numpy as np
import os
import pickle
import PIL as Image
# formtakepicture----------------------------------------
from tkinter import *
#defining login function

def Loginform():
    global login_screen
    login_screen = Tk()
    #Setting title of screen
    login_screen.title("Form sinh viên")
    #setting height and width of screen
    login_screen.geometry("400x160+500+300")
    #declaring variable
    global  message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    #Creating layout of login form
    Label(login_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    #Username Label
    Label(login_screen, text="Tên Sinh Viên : ").place(x=20,y=40)
    #Username textbox
    Entry(login_screen, textvariable=username).place(x=110,y=42)
    #Password Label
    Label(login_screen, text="Mã Sinh Viên : ").place(x=20,y=80)
    #Password textbox
    Entry(login_screen, textvariable=password ).place(x=110,y=82)
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message).place(x=95,y=100)
    #Login button
    Button(login_screen, text="Submit", width=10, height=1, bg="orange",command=login).place(x=105,y=130)
    login_screen.mainloop()
#calling function Loginform

def login():
   
    #getting form data
    uname=username.get()

    pwd=password.get()
    #applying empty validation
    if uname=='' or pwd=='':
        message.set("Không được để trống")
    elif pwd.isdecimal()== False:
        message.set("Mời bạn nhập lại mã sinh viên")
    else:
        login_screen.destroy()
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        cam = cv2.VideoCapture(0)
        detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # Enrollment = txt.get()    
        # Name = txt2.get()     
        #tao folder
        parent_dir = "E:/python/nhandienkhuonmat/src/images"

        #E:/python/nhandienkhuonmat/src/images
        # Path 
       
        #duong dan folder
        path = os.path.join(parent_dir, uname) 
        #check duogn dan
        isdir = os.path.isdir(path) 
        print(path) 
        #defining loginform function
        if(isdir==False):
        # Create the directory 
            os.makedirs(path) 
        print("Directory '% s' created" % uname) 
      
        sampleNum = 0
        cap= cv2.VideoCapture(0)
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret,frame=cam.read()
            #roi_color=frame[y:y+h,x:x+w]
            faces= face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # incrementing sample number
                sampleNum = sampleNum + 1
            # saving the captured face in the dataset folder
                last_path=parent_dir+"/"+uname+"/"+uname+"-"+pwd + '.' + str(sampleNum) + ".jpg"
                cv2.imwrite( last_path,gray[y:y + h, x:x + w])
            cv2.imshow('Frame', img)
            # wait for 100 miliseconds
            if cv2.waitKey(900) & 0xFF == ord('q'):
                break
                        # break if the sample number is morethan 100
            elif sampleNum > 5:
                break   
        import pymsgbox
        pymsgbox.alert('Them anh thanh cong!', 'Title')
        cam.release()
        cv2.destroyAllWindows()	
# -------------------------------------------------------------------
Loginform()

