from sys import argv
import os
import time
import datetime
import psutil
from email.message import *
import MyGmailAppPassword
from  smtplib import SMTP_SSL
import ssl 
import pandas as pd

def Process_Log():

    extention =(time.ctime().replace(" ","_")).replace(":","-")
    File_Name = "ProcessLog_{}.csv".format(extention)

    list =[]
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            list.append(pinfo)

        except(Exception):
            pass
    df = pd.DataFrame(list)
    df[['pid','name','username']].to_csv(File_Name,index=True)

    return File_Name

def Send_Email(Email_id,Process_File):
            
        email_sender = "akshayaher5555@gmail.com"
        email_password = MyGmailAppPassword.Password
        email_receiver = Email_id
        Time = str (datetime.datetime.now())
        Subject ="Process Log File : "+Time
        body ="""
        Hello,

        Hope your doing well,

        Please Find my attached Process Log File.

        Regards,
        Akshay Aher

        """
    
        em = EmailMessage()

        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = Subject
        em.set_content(body)

        fd =  open(Process_File,'rb')
        file_data = fd.read()
        file_name = fd.name
        file_type = file_name.split('.')

        em.add_attachment(file_data,maintype = "application",subtype=file_type[1], filename=file_name)

        Context = ssl.create_default_context()

        with SMTP_SSL('smtp.gmail.com',465, context =Context) as smtp:  
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender,email_receiver,em.as_string())
            print("Email Sent to ",email_receiver)

def main():

    print("\nMavellous Process Log")
        
    if(len(argv) !=2):
        print("Invalid Number of Arguments")
        exit()

    if(argv[1]=="-h" or argv[1]=="-H"):
        print("This Application accept Folder_Name and create running process log file in that folder ")
        exit()

    if(argv[1]=="-u" or argv[1]=="-U"):
        print("Usage : <Application_Name> <Receiver_Email_Id>")
        exit()

    try:
        Process_File = Process_Log()
        Send_Email(argv[1],Process_File)

    except(Exception):
        print("Invalid Input")
     
    
if __name__ =="__main__":
    main()    