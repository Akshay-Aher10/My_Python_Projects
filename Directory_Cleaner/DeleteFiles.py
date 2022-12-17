import os

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

    # else:
    #     pfd.write("No Duplicate Files Found. :"+str(time.ctime())+"\n")
    #     #print("No Duplicate Files Found.")