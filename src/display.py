from calendar import setfirstweekday
from importlib.resources import path
from re import X
from tkinter import S
from turtle import pos
from warnings import catch_warnings
from cv2 import resize
import pygame
from pygame.locals import *
# import thu vien gui mail
import smtplib,ssl
import smtplib
from email.message import EmailMessage


pygame.init()


window_width=1000
window_height=700

screen = pygame.display.set_mode((window_width, window_height))
# Set title to the window
pygame.display.set_caption("Nhận diện khuôn mặt")

font = pygame.font.SysFont('Constantia', 30)
# Open a window

size = (window_width, window_height)
screen = pygame.display.set_mode(size)
#define colours

red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

#define global variable
clicked = False
counter = 0
background_image = pygame.image.load("E:/python/nhandienkhuonmat/bg1.png")
resized_background = pygame.transform.scale(background_image, (window_width, window_height))
class button():
        
    #colours for button and text
    button_col = (25, 202, 202)
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = red#mau chu
    width = 180
    height = 70

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
    def draw_button(self):

        global clicked
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #create pygame Rect object for the button
        button_rect = Rect(self.x, self.y, self.width, self.height)
        
        #check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)
        
        #add shading to button
        pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        #add text to button
        font = pygame.font.SysFont('Times New Roman', 15)
        text_img = font.render(self.text, True, self.text_col)

        

        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action
class image():
    def __init__(self,x,y,path) :
        self.x=x
        self.y=y
        self.path=path
        # self.path=path
    def set_image(self):
        icon_image=pygame.image.load(self.path)
        resized_background = pygame.transform.scale(icon_image, (180, 150))
        screen.blit(resized_background, [self.x, self.y])

class logo():
    def __init__(self,x,y,path) :
        self.x=x
        self.y=y
        self.path=path
    def set_logo(self):
        icon_image=pygame.image.load(self.path)
        resized_background = pygame.transform.scale(icon_image, (50, 50))
        screen.blit(resized_background, [self.x, self.y])
again = button(100, 500, 'QUÉT GƯƠNG MẶT')

train = button(400, 500, 'TRAIN FACES')

anh = button(700, 500, 'THÊM ẢNH')
sendfile = button(100, 200, 'GỬI FILE')

image1=image(100,320,'E:/python/nhandienkhuonmat/src/face-scan.png')
image2=image(400,320,'E:/python/nhandienkhuonmat/src/face-train.png')
image3=image(700,320,'E:/python/nhandienkhuonmat/src/camera-icon.png')
image4=logo(50,50,'E:/python/nhandienkhuonmat/src/Logo.png')
image5=image(100,50,'E:/python/nhandienkhuonmat/file.png')
# ---------send email-------------------------------------------------------------
SENDER_EMAIL = "sovait99@gmail.com"
APP_PASSWORD = "frpphomnapoqntqv"
def send_mail_with_excel(recipient_email, subject, content, excel_file):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_email
    msg.set_content(content)

    with open(excel_file, 'rb') as f:
        file_data = f.read()
    msg.add_attachment(file_data, maintype="application", subtype="xlsx", filename=excel_file)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        try:
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
            import pymsgbox
            pymsgbox.alert("Successfully sent email", 'Thông báo')        
        except Exception:
            import pymsgbox
            pymsgbox.alert("Error: unable to send email", 'Thông báo') 
       

# -------------------------form gui mail-----------------------------------
from tkinter import *
#defining login function
def login():
    #getting form data
    uname=username.get()
    #applying empty validation
    if uname=='' :
       
        import pymsgbox
        pymsgbox.alert('Email khong thể bỏ trống', 'Thông báo')        
    else:
        send_mail_with_excel(uname,"hello","aaa",'E:/python/nhandienkhuonmat/src/sample_data2.xls')
    #   if uname=="abcd@gmail.com" and pwd=="abc123":
    #    message.set("Login success")
    #   else:
    #    message.set("Wrong username or password!!!")
        
#defining loginform function
def Loginform():
    global login_screen
    login_screen = Tk()
    
    #Setting title of screen
    login_screen.title("Email Form")
    #setting height and width of screen
    login_screen.geometry("400x200+500+300")
    #declaring variable
    global  message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    #Creating layout of login form
    Label(login_screen,width="300", text="Mời nhập email bạn muốn gửi", bg="orange",fg="white").pack()
    #Username Label
    Label(login_screen, text="EMAIL NGƯỜI NHẬN ").place(x=20,y=50)
    Label(login_screen, text="Email sẽ được gửi tự động cho giáo viên mỗi 45 phút").place(x=20,y=100)
    #Username textbox
    Entry(login_screen, textvariable=username).place(x=150,y=50)
  
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message).place(x=95,y=100)
    #Login button
    Button(login_screen, text="Gửi", width=10, height=1, bg="orange",command=login).place(x=150,y=150)
    login_screen.mainloop()
#calling function Loginform

#---------------------------------------------------------------------------

run = True
while run:
    
    screen.blit(resized_background, [0, 0])
    image1.set_image()
    image2.set_image()
    image3.set_image()
    image4.set_logo()
    image5.set_image()
    if again.draw_button():
        # import faces
        import faces2
    if train.draw_button():
        import facestrain
    if sendfile.draw_button():
       Loginform()
        # send_mail_with_excel("phucvinhfnt@gmail.com","hello","aaa",'sample_data2.xls')


    if anh.draw_button():
        import takepicture		
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False	
    pygame.display.update()


pygame.quit()
