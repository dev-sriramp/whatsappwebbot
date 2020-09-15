from os import environ ,system,name
import pip
import importlib
import platform
import os

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

def module():
    #this function is to check for the module if not present it install and import it
    try:
        importlib.import_module("time")
    except ModuleNotFoundError:
        try:
            pip3.main(['install', "time"])
        except:
            pip.main(['install', "time"])
    finally:
        global time
        import time
    try:
        importlib.import_module("selenium")
    except ModuleNotFoundError:
        try:
            pip3.main(['install', "selenium"])
        except:
            pip.main(['install', "selenium"])
    finally:
        global selenium
        import selenium
    try:
        importlib.import_module("pyautogui")
    except ModuleNotFoundError:
        try:
            pip3.main(['install', "pyautogui"])
        except:
            pip.main(['install', "pyautogui"])
    finally:
        global pyautogui
        import pyautogui
        
def phonenumber():
    #this function read the phone number from "phonenumber.txt" files
    file = open('phonenumber.txt', 'r') 
    return file.readlines()
    
    
def message():
    #this function read the message from "message.txt" files
    file = open('message.txt', 'r') 
    return file.read()

def message_sent():
    #this is the main part of the program to send message
    try:
        global time
        import time
        global pyautogui
        import pyautogui
        browser.get(("https://web.whatsapp.com/send?phone={}&text={}").format(i,text_message))
        time.sleep(5)
        if(picture=="y" or picture=="Y"):
            photo = browser.find_element_by_css_selector("div[title='Attach']")
            time.sleep(5)
            photo.click()
            time.sleep(5)
            oldphoto = browser.find_element_by_css_selector("button[class='_1dxx-']")
            time.sleep(5)
            oldphoto.click()
            time.sleep(5)
            pyautogui.write(pic)
            pyautogui.press('enter')
            time.sleep(5)
            send = browser.find_element_by_css_selector("div[class='_6TTaR']")
            time.sleep(5)
            send.click()
            print(i)
            time.sleep(5)
            
        else:
            send=browser.find_element_by_css_selector("button[class='_1U1xa']")
            send.click()
            print(i)
            time.sleep(5)
        print(("Message send to {}").format(int(i)))
    except:
        print(("Message Not send to {}").format(int(i)))
        not_send=open("notsend","a+")
        not_send.write("%d\r\n" % int(i))
        not_send.close()
        print("Not_send file is created for those whatsapp mesage not send")
    
def login(browser):
    global time 
    import time
    browser.get("https://web.whatsapp.com")
    time.sleep(10)
    global phone_number
    phone_number=phonenumber()
    global text_message
    text_message=message()
    global i
    for i in phone_number:
        i="".join(str(x) for x in i)
        message_sent()
    browser.get("https://web.whatsapp.com")
    time.sleep(100)
    
def main():
    is_android="ANDROID_STORAGE" in environ
    if(is_android):
        clear()
        print("ANDROID Device Not Supported")
    else:
        clear()
        global web_driver
        print("Before you executing the program you need to download chrome web driver")
        web_driver=input("Path to the chrome web driver : ")
        module()
        clear()
        global picture
        global pic
        pic=None
        print("want to insert picture ?")
        picture=input("Y for YES and N for NO  : ")
        if(picture=="Y" or picture=="y"):
            print("image location must be on local computer")
            pic=input("Enter your image path : ")
        clear()
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        global browser
        browser = webdriver.Chrome(executable_path=web_driver)
        login(browser)

main()


#This code is written by uniqueredhat
#code contributers SRIRAM P , SANJAY R , UDHAYAKUMAR T , THAVAMUTHUBASKARAN L
