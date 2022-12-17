import time
import os

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

    # else:
    #     #print("No  Duplicate files Found")

    return File_Path,DupFileCount   
