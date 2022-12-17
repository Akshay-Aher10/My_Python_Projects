import hashlib
import os

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

    # else:
    #     pfd.write("Invalid Path",str(time.ctime()))
    #     #print("Invalid Path"+time)
    return dups,File_Count     
