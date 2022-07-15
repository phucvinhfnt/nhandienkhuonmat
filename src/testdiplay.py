import tkinter
from tkinter import *
from tkinter import ttk
import numpy as np
from PIL import Image, ImageTk
import cv2
from tkinter.constants import *
from tkinter.scrolledtext import ScrolledText
import face_recognition
import cv2
import numpy as np

ikkuna=tkinter.Tk()
ikkuna.title("Nhận diện khuôn mặt")

frame=np.random.randint(0,255,[100,100,3],dtype='uint8')
img = ImageTk.PhotoImage(Image.fromarray(frame))

image_camera=tkinter.Label(ikkuna) #,image=img)
image_camera.grid(row=0,column=0,columnspan=3,pady=1,padx=10)

message=""
paneeli_text=tkinter.Label(ikkuna,text=message)
paneeli_text.grid(row=1,column=1,pady=1,padx=10)
images = []

text = ScrolledText(ikkuna, wrap=WORD)
text.grid(row=0,column=3 ,padx=10,sticky=tkinter.NE, pady=2)

img2 = Image.open("E:/python/nhandienkhuonmat/bg1.png").resize((100, 80), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(img2)
# images.append("C:\Users\LHI\Desktop\nhandienkhuonmat\src\4.png")
svname="Ho Van Phuc Vinh"
Masv="11171052109"


#hien thi ma so sinh vien va anh o day------------------
text.image_create(INSERT,padx=5, pady=5, image=img2)#anh
text.insert(INSERT,'\n'+svname+'\n'+Masv+'\n')#chu
text.insert(INSERT,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'+'\n')#chu
text.image_create(INSERT,padx=5, pady=5, image=img2)#anh
text.insert(INSERT,'\n'+svname+'\n'+Masv+'\n',)#chu
text.insert(INSERT,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'+'\n')#chu
text.image_create(INSERT,padx=5, pady=5, image=img2)#anh
text.insert(INSERT,'\n'+svname+'\n'+Masv+'\n')#chu
text.insert(INSERT,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'+'\n')#chu
text.image_create(INSERT,padx=5, pady=5, image=img2)#anh
text.insert(INSERT,'\n'+svname+'\n'+Masv+'\n')#chu
text.insert(INSERT,'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'+'\n')#chu
text.image_create(INSERT,padx=5, pady=5, image=img2)#anh
text.insert(INSERT,'\n'+svname+'\n'+Masv+'\n')#chu


global cam

# --------------------------------------------------------
# fat hien khuon mat
# Bai toan nhan dang don gian su dung thu vien face recognition tu webcam cua banl resolution)
video_capture = cv2.VideoCapture(0)

# Load a hinh anh de may hoc va ghi nho nham muc dich xac nhan danh tinh
mautc_image = face_recognition.load_image_file("E:/python/nhandienkhuonmat/mau1.jpg")
mautc_face_encoding = face_recognition.face_encodings(mautc_image)[0]

# Load anh thu hai
# phouvanh_image = face_recognition.load_image_file("phouvanh.jpg")
# phouvanh_face_encoding = face_recognition.face_encodings(phouvanh_image)[0]

# Load anh thu ba
# nanar_image = face_recognition.load_image_file("nanar.jpg")
# nanar_face_encoding = face_recognition.face_encodings(nanar_image)[0]

# Tao mang ten lien quan den khuon mat da load
known_face_encodings = [
    mautc_face_encoding,
    # phouvanh_face_encoding,
    # nanar_face_encoding
]
known_face_names = [
    "MauTC",
    # "Phouvanh"
    # "Nanar nanar"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
# -------------------------------------------------
def otakuva():
    global frame
    global cam
    cam = cv2.VideoCapture(0)
    #cv2.namedWindow("Experience_in_AI camera")
    while True:
        ret, frame = cam.read()

        #Update the image to tkinter...
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        img_update = ImageTk.PhotoImage(Image.fromarray(frame))
        image_camera.configure(image=img_update)
        image_camera.image=img_update
        image_camera.update()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)
        process_this_frame = not process_this_frame
    # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

        # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # message="listbox here"
        # paneeli_text1=tkinter.Label(ikkuna,text=message)
        # paneeli_text1.grid(row=0,column=3,pady=1,sticky=tkinter.NE,padx=70) 
        if not ret:
            print("failed to grab frame")
            break

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")

            cam.release()
            cv2.destroyAllWindows()
            break

def stopcam():
    global cam
    cam.release()
    cv2.destroyAllWindows()
    print("Stopped!")

painike_korkeus=10
painike_1=tkinter.Button(ikkuna,text="Start",command=otakuva,height=5,width=20)
painike_1.grid(row=1,column=0,pady=10,padx=10)
painike_1.config(height=1*painike_korkeus,width=20)

painike_korkeus=10
painike_1=tkinter.Button(ikkuna,text="Stop",command=stopcam,height=5,width=20)
painike_1.grid(row=1,column=2,pady=10,padx=10)
painike_1.config(height=1*painike_korkeus,width=20)
ikkuna.mainloop()