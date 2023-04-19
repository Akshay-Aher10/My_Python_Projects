from sys import argv
import time
import hashlib
import os
import schedule
from Email_Script import Send_Email

pfd = open('Process_Log.txt','a')

def hashfile(path, blocksize =1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    
    while(len(buf)>0):
        hasher.update(buf)
        buf = afile.read(blocksize)

    afile.close()

    return hasher.hexdigest()

def findDup(path,extention):

    flag = os.path.isabs(path)

    if flag ==False:
        path  = os.path.abspath(path)

    exists = os.path.isdir(path)

    File_Count = 0
    dups ={}
    if exists:
        for dirName, subDirs, fileList in os.walk(path):

            
            for file in fileList:
                
                if(extention =='All' or extention =='all' or extention =='ALL'):
                    path = os.path.join(dirName,file)
                    file_hash = hashfile(path)

                    if file_hash in dups:
                        dups[file_hash].append(path)    
                    else:
                        dups[file_hash]=[path]
   
                else:
                    
                    if(file.endswith(extention)):
                        path = os.path.join(dirName,file)
                        file_hash = hashfile(path)

                        if file_hash in dups:
                            dups[file_hash].append(path)    
                        else:
                            dups[file_hash]=[path]
                
                File_Count+=1

    else:
        pfd.write("Invalid Path",str(time.ctime()))
        #print("Invalid Path"+time)
    return dups,File_Count     

def DeleteFiles(dict1):
    results = list(filter(lambda x: len(x) >1,dict1.values()))

    icnt = 0

    if len(results)>0:

            for result in results:
                for subresult in result:
                    icnt+=1
                    if icnt >=2:
                        os.remove(subresult)
                icnt = 0        

    else:
        pfd.write("No Duplicate Files Found. :"+str(time.ctime())+"\n")
        #print("No Duplicate Files Found.")

        
def Get_Log_File(dict1,Folder_Name = "Marvellous"):
    Current_dirPath = os.getcwd()
    Folder_path = os.path.join(Current_dirPath,Folder_Name)
    Folder_Exist = os.path.isdir(Folder_path)

    if(Folder_Exist ==False):
        os.mkdir(Folder_Name)
        
    Folder_path =os.path.abspath(Folder_Name)

    Time =(time.ctime().replace(" ","_")).replace(":","-")
    File_Name = "DeleteFilelog_{}.txt".format(Time)

    File_Path = os.path.join(Folder_path,File_Name)
    
    fd =open(File_Path,'a')
    cnt = 1
    DupFileCount =0
    results = list(filter(lambda x:len(x)>1,dict1.values()))

    if len(results)>0:

        for result in results:
            for subresult in result:
                fd.write(str(cnt)+"] "+subresult+'\n')
                cnt+=1
                DupFileCount+=1

    else:
        pfd.write("No Duplicate Files Found. :"+str(time.ctime())+"\n")
        #print("No  Duplicate files Found")

    return File_Path,DupFileCount   

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
        time.sleep(60)

if __name__=="__main__":
    main()