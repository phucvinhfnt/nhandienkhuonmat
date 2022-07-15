from tkinter import*

#Create an instance of tkinter frame
win= Tk()

#Define geometry of the window
win.geometry("750x250")

OPTIONS = [
"Lập Trình Ứng Dụng",
"Xử Lý Ảnh",
"An Toàn Bảo Mật Thông Tin"
]



variable = StringVar(win)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(win, variable, *OPTIONS)


def ok():
    print ("value is:" + variable.get())


    
#Define a function to close the popup window
def close_win(top):
   top.destroy()
def insert_val(e):
   e.insert(0, "Hello World!")

#Define a function to open the Popup Dialogue
def popupwin():
   #Create a Toplevel window
   top= Toplevel(win)
   top.geometry("750x250")

   #Create an Entry Widget in the Toplevel window
   #entry= Entry(top, width= 25)
  
   #entry.pack()
   e_text="entry.get()"
   Label(top, text=e_text, font= ('Century 15 bold')).pack(pady=20)
   #Create a Button to print something in the Entry widget
   #Button(top,text= "Insert", command= lambda:insert_val(e_text)).pack(pady= 5,side=TOP)
   #Create a Button Widget in the Toplevel Window
   button= Button(top, text="Ok", command=lambda:close_win(top))
   button.pack(pady=5, side= TOP)
#Create a Label
label= Label(win, text="Mời nhập tên môn học", font= ('Helvetica 15 bold'))
label.pack(pady=15)
#creat a dropdown list
dropdown= OptionMenu(win, variable, *OPTIONS)
dropdown.pack(pady=15)
#Create a Button
button= Button(win, text= "Submit!", command= popupwin, font= ('Helvetica 14 bold'))
button.pack(pady=20)
win.mainloop()