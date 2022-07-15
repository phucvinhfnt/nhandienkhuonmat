import smtplib
import ssl
from email.message import EmailMessage

# Define email sender and receiver
# email_sender = 'sovait99@gmail.com'
# email_password = 'frpphomnapoqntqv'
# email_receiver = 'phucvinhfnt@gmail.com'

# # Set the subject and body of the email
# subject = 'Check out my new video!'
# body = """

# """

# em = EmailMessage()
# em['From'] = email_sender
# em['To'] = email_receiver
# em['Subject'] = subject
# em.set_content(body)

# # Add SSL (layer of security)
# context = ssl.create_default_context()
# with open("E:/python/nhandienkhuonmat/src/123.xlsx", 'rb') as f:
#         file_data = f.read()
# em.add_attachment(file_data, maintype="application", subtype="xlsx", filename="E:/python/nhandienkhuonmat/src/sample2.xlsx")
# # Log in and send the email
# with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#     smtp.login(email_sender, email_password)
#     smtp.sendmail(email_sender,email_receiver, em.as_string())
SENDER_EMAIL = "sovait99@gmail.com"
APP_PASSWORD = "frpphomnapoqntqv"
email_receiver = 'phucvinhfnt@gmail.com'
def send_mail_with_excel(recipient_email, subject, content, excel_file):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_email
    msg.set_content(content)
    APP_PASSWORD = "frpphomnapoqntqv"
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
       
send_mail_with_excel(SENDER_EMAIL,email_receiver,"aaa",'E:/python/nhandienkhuonmat/src/123.xlsx')
# -------------------------form gui mail-----------------------------------
