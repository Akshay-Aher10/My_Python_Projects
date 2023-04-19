from email.message import EmailMessage
from smtplib import SMTP_SSL
import ssl
from MyGmailAppPassword import Password

def Send_Email(Email_ID,startTime,File_Count,DupFile_Count,Total_ProcessTime,File_Name):

   Emailer_Sender = 'akshayaher5555@gmail.com'
   Email_Password = Password
   Email_Receiver = Email_ID
   Subject = "Duplicate Files Tracker"
   Body = '''
   Hello User,

   Please Find the Statistics about the operation of duplicate file removal.
      > Starting Time of Scanning : {no1}
      > Total Number of File Scanned : {no2}
      > Total Number of Duplicate files Found : {no3}
      > Total process Time : {no4} Second.

   Regards,
   Akshay Aher
   
   '''.format(no1=startTime,no2=File_Count,no3=DupFile_Count,no4=Total_ProcessTime)

   EM = EmailMessage()

   EM['To']= Email_Receiver
   EM['From']= Emailer_Sender
   EM['Subject'] = Subject
   EM.set_content(Body)

   fd = open(File_Name,'rb')
   File_Data = fd.read()
   File_Name = fd.name
   File = File_Name.split(".")

   EM.add_attachment(File_Data, maintype='file', subtype=File[1] ,filename=File_Name)

   Context = ssl.create_default_context()

   smtp = SMTP_SSL('smtp.gmail.com',465,context =Context)
   smtp.login(Emailer_Sender,Email_Password)
   smtp.sendmail(Emailer_Sender,Email_Receiver,EM.as_string())
   print("Email Sent : ",Email_Receiver)

