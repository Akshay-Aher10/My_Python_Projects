import webbrowser
import time

def open_url():
        
    Url_List = ('https://docs.google.com/spreadsheets/d/1Zj89XvmMNrSGPUVIwVwlZQGXIZ08Lj9j6x6Zg-RbGdE/edit#gid=0',
    'https://docs.google.com/spreadsheets/d/18MSGXmzcGgm7_2IxUOSacaWWzO5oLwJrnLF-tsgz5Oc/edit#gid=0',
    'https://docs.google.com/spreadsheets/d/1UL3kyR9-KsEks7qB35MxiARmioxzqYv026Wg4uF2CCo/edit#gid=0',
    'https://docs.google.com/spreadsheets/d/1zMc9icBog4fzUbKalK6cR3QCrBKguZ1_Z6odbtVsZvM/edit#gid=1797013058',
    'https://docs.google.com/spreadsheets/d/11X8At-onGi9BvwtnJ43ysv4Q8XxxNmb94npFUtb71PQ/edit#gid=0',
    'https://docs.google.com/spreadsheets/d/1teBjNdZX6q3uX0mFcEnN6oefzUerDUwwt7S6cTlHC9A/edit#gid=0')

    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    webbrowser.register('chrome',None, webbrowser.BackgroundBrowser(chrome_path))
    browser = webbrowser.get('chrome')

    for url in Url_List:
        
        browser.open_new_tab(url)
        time.sleep(5)

def main():
    open_url()
    
if __name__=="__main__":
    main()    

