import pyttsx3
import PyPDF2
from sys import argv

def Audio_Speaker(PDF_Reader,PageNumber):

    page = PDF_Reader.getPage(PageNumber)
    text = page.extractText()
    speaker = pyttsx3.init()
    print("Author is Speaking.....")
    speaker.say(text)
    speaker.runAndWait()

def Pdf_Reader(File_Name):
    book = open(File_Name,'rb')
    PDF_Reader = PyPDF2.PdfFileReader(book)
    Pages = PDF_Reader.numPages
    return PDF_Reader,int(Pages)

def Drawer(File_Name):

    separator = "-"*30
    PDF_Reader,Pages = Pdf_Reader(File_Name)

    while(True):
        
        print('''
        Choose Options
        1. Total Book Pages
        2. Selete Page Number to Listen
        3. Close Application
        ''')

        Option =input("Enter Option Number : ")

        if(Option =='1'):
            print(separator)
            print("Total No of Pages : ",Pages)
            print(separator)
            continue

        elif(Option =='2'):
            PageNumber = int(input("Enter Page Number to Listen\n"))
            if(PageNumber>=1 and PageNumber<=Pages):

                Audio_Speaker(PDF_Reader,(PageNumber-1))

                print("\n------------------------ you are on {} page.\n".format(PageNumber))
                while(PageNumber<=Pages):
                    Ans =input('Want Read Next page : Y / N \n')
                    if(Ans == 'Y' or Ans == 'y'):
                        PageNumber+=1
                        Audio_Speaker(PDF_Reader,(PageNumber-1))
                        
                        print("\n------------------------ you are on {} page.\n".format(PageNumber))
                    else:
                        break
            else:
                print(separator)
                print("invalid Page Number")
                print(separator)
                continue

        elif(Option =='3'):
            print(separator)
            print("Thank you....")
            print(separator)
            exit()

        else:
            print(separator)
            print("Please Enter valid Option number")
            print(separator)
            continue    

def main():
        
    print("--------Audio Book Speaker--------")
    print("Application Name :"+argv[0])

    if(len(argv)!=2):
        print("Error : Invalid Number of Arguments")
        exit()
    if(argv[1]=="-h" or argv[1]=="-H"):
        print("This Script is used to Listen pdf book")
        exit()
    if(argv[1]=='-u' or argv[1]=='-U'):
        print("Usage : <Application_Name> <AbsolutePath_of_pdf>")
        exit
        
    try:
        Drawer(argv[1])

    except Exception:
        print("Error : Invalid Input")     

if __name__=="__main__":
    main()