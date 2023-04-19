from sys import argv
import time
import schedule
from Email_Script import Send_Email
from findDup import findDup
from DeleteFiles import DeleteFiles
from Get_Log_File import Get_Log_File
 

def Start_Task(Folder_Path,File_Extention,Email_ID):
    try:
        
        arr = {}
        startTime = time.time()
        Time = time.ctime()
        arr,File_Count = findDup(Folder_Path,File_Extention)
        File_Path,DupFile_Count = Get_Log_File(arr)
        DeleteFiles(arr)

        endTime = time.time()

        Total_ProcessTime = endTime-startTime

        Send_Email(Email_ID,Time,File_Count,DupFile_Count,Total_ProcessTime,File_Path)
        
    except ValueError:
        pass
    except Exception as E:
        pass

def main():
    
    print("\n--- Marvellous Directory Automation ---")
    print("Applicayion Name : " + argv[0])

    if(len(argv)!=5):
        print("Error : invalid number of arguments")
        exit()
    
    if(argv[1]=="-h" or argv[1]=="-H"):
        print("This Script is used to traverse specific directory and Delete Duplicate Files")
        exit()

    if(argv[1]=="-u" or argv[1]=="-U"):
        print("Usage : <Application_Name> <AbsPath_of_Directory> <Extention> <Duration> <Email_ID>")
        exit()
        
    Folder_Path = argv[1]
    File_Extention = argv[2]
    Duration = int(argv[3])
    Email_ID = argv[4]


    Start_Task(Folder_Path,File_Extention,Email_ID)
    schedule.every(Duration).minutes.do(Start_Task,Folder_Path,File_Extention,Email_ID)

    while(True):
        schedule.run_pending()
        time.sleep(20)

if __name__=="__main__":
    main()