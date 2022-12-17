import webbrowser
import time
from sys import argv

def open_url(File):
    
    fd = open(File,'r')
    

    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    webbrowser.register('chrome',None, webbrowser.BackgroundBrowser(chrome_path))
    browser = webbrowser.get('chrome')

    for url in fd.readlines():
        
        browser.open_new_tab(url)
        time.sleep(5)

def main():

    print("--------URL Opener--------")

    print("Application Name :"+argv[0])

    if(len(argv)!=2):
        print("Error : Invalid Number of Arguments")
        exit()
    if(argv[1]=="-h" or argv[1]=="-H"):
        print("This Script is used to open urls from given files")
        exit()
    if(argv[1]=='-u' or argv[1]=='-U'):
        print("Usage : <Application_Name> <AbsolutePath_of_file>")
        exit
        
    try:
        open_url(argv[1])

    except Exception:
        print("Error : Invalid Input")  
    
if __name__=="__main__":
    main()    

