import os                              # folder_path varun files kadnya sathi use kela ahe (Line 17)
from email.message import EmailMessage # EmailMessage class : Email cha header fild and body set ani access karnya sathi \ Line 10 la object create kela ahe 
import ssl                             # for secures communications(Line 27)
import smtplib                         # actual module to send email using SMTP(Line 29)
import MyGmailAppPassword              # user define gmail AppPassword ahe.(Line 37)


def SendEmail(email_sender,email_receiver,Subject,body,email_password):

    
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
            for Receiver in email_receiver:
                smtp.sendmail(email_sender,Receiver,em.as_string())    # em.as_string() :Converts the Multipart msg into a string
                print("Email Sent to ",Receiver)

def main():

    email_sender = "akshayaher5555@gmail.com"
    email_password = MyGmailAppPassword.Password
    Receiver = ['deepprajapati01@gmail.com','aher.akshay101@gmail.com','kalepratik999@gmail.com','Rohitaher2@gmail.com']

    Subject ="Sending Email using Python"
    body ="""

    Hello,

    Hope your doing well,

    Please Find the Attached Documents for your Reference

    Regards,
    Akshay Aher

    """
    SendEmail(email_sender,Receiver,Subject,body,email_password)

if __name__ =="__main__":
    main()