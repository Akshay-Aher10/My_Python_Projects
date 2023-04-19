from email.message import EmailMessage 
import ssl                             
import smtplib                         
import MyGmailAppPassword              
import pandas as pd
import datetime


def SendEmail(email_sender,email_receiver,Subject,body,email_password):
    em = EmailMessage()

    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = Subject
    em.set_content(body)

    #---------------------------below part is for Attachment Purpose----------------------------------------------#
    #
    # list  = os.listdir(r'C:\Users\dell\Desktop\Python\Email_Sender\Files')
    #
    # for File in list:
    #     with open(File,'rb') as F:    #rb = read
    #         file_data = F.read()
    #         file_name = F.name
    #         file_type = file_name.split('.')
    #
    #     em.add_attachment(file_data,maintype = "application",subtype=file_type[1], filename=file_name)
    #
    #-------------------------------------------------------------------------------------------------------------#

    Context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465, context =Context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())
        print("Email Sent to :",email_receiver)


def main():

    email_sender = "akshayaher5555@gmail.com"
    email_password = MyGmailAppPassword.Password

    Data = pd.read_csv("BIrthday_list4.csv")

    time = datetime.datetime.now().strftime("%d-%m")

    for index,item in Data.iterrows():

        birthdate=item['BirthDate']

        Subject ="Many Many Happy Returns of day "+(item['Name'])

        body ="""
        Dear {}
           
        Like you, your special day is also important for us. 
        i am sending you my heartiest and sincerest wishes on your birthday enjoy your day to the fullest and have the brightest year ahead.
        looking forward to our strong relationship and bonding for the next number of upcoming years.
        Happy birthday once again....

        Regards,
        Akshay Aher

        """.format(item['Name'])

        if(time == birthdate):
            SendEmail(email_sender,item['Email'],Subject,body,email_password)
            SendWhatsAppMsg()


if __name__ =="__main__":
    main()