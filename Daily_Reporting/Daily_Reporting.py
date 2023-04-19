from email.message import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import MyGmailAppPassword
from  smtplib import SMTP_SSL
import ssl

import pandas as pd

def Create_Table(Project_Name,Target,Login_Time):
    
    t1 = pd.DataFrame({ 'Project_Name' :["  "+Project_Name+"  "],
                        'Target' : [" "+Target+" "]
                        },index=None)
    
    t2 = pd.DataFrame({"Login_Time" :["  "+Login_Time+"AM"+"  "] })

    t1.index += 1
    t2.index += 1

    html1 = t1.to_html()
    html2 = t2.to_html()

    return html1,html2

def Send_Email(Table1,Table2):
            
        email_sender = "akshay.aher@bizkonnectsolutions.com"
        email_password = MyGmailAppPassword.Password
        email_receiver1 = 'hr@bizkonnect.com'
        email_receiver2 = 'fareed.khan@bizkonnect.com'

        Subject ="Daily_Reporting : Akshay Aher."
        text ="Hello Sir, \nPlease find below my POA Report\n\n"
        text1 ="\n"
        text2 = "Regards,\nAkshay Aher"

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(Table1, 'html')
        part3 = MIMEText(text1, 'plain')
        part4 = MIMEText(Table2, 'html')
        part5 = MIMEText(text1, 'plain')
        part6 = MIMEText(text2, 'plain')

        msg = MIMEMultipart()
        msg['Subject'] = Subject
        msg['From'] = email_sender
        msg['To'] = email_receiver1
        msg['Cc'] = email_receiver2
        msg.attach(part1)
        msg.attach(part2)
        msg.attach(part3)
        msg.attach(part4)
        msg.attach(part5)
        msg.attach(part6)
        
        Context = ssl.create_default_context()

        with SMTP_SSL('smtp.gmail.com',465, context =Context) as smtp:  
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender,(email_receiver1,email_receiver2),msg.as_string())
            print("Email Sent Successfully..")

def main():

    Value = input("\nGood Moring Akshay ! Are your Working today? : \n")

    if(Value == 'y' or Value =='Y'):
        Project_Name = input("\nOn Which project are you going to work today?\n")
        Target = input("\nToday's Target ?\n")
        Login_Time = input("\nToday's Login time ?\n")

        Table1,Table2 = Create_Table(Project_Name,Target,Login_Time)
    else:
        print("Cancelled Reporting Mail")

    Value = input("Do you want send Report?(y/n) : ")

    if(Value == 'Y' or Value == 'y'):
         Send_Email(Table1,Table2)
            

if __name__ == "__main__":
    main()