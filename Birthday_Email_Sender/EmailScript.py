import os
from email.message import EmailMessage
import ssl
import smtplib
import MyGmailAppPassword

email_sender = "akshayaher5555@gmail.com"
email_password = MyGmailAppPassword.Password #os.environ.get("EMAIL_PASSWORD")
email_receiver = ['deepprajapati01@gmail.com','aher.akshay101@gmail.com','kalepratik999@gmail.com']

Subject ="Sending Email using Python"
body ="""

Hello,

Hope your doing well,

Please Find the Attached Excel Sheet for your Reference

Regards,
Akshay Aher

"""

em = EmailMessage()


em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = Subject
em.set_content(body)

list  = os.listdir(r'C:\Users\dell\Desktop\Python\Email_Sender\Files')

for File in list:
    with open(File,'rb') as F:    #rb = read
        file_data = F.read()
        file_name = F.name
        file_type = file_name.split('.')

    em.add_attachment(file_data,maintype = "application",subtype=file_type[1], filename=file_name)

Context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context =Context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())    # em.as_string() :Converts the Multipart msg into a string
    print("Email Sent...")
