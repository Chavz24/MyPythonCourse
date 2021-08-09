#abre el brave browser en https://login.metafilter.com/, scribe un nombr de usaurio
#una contrasena y da submit.

from selenium import webdriver
import logging

open('mylog.txt','w').write('\n')
logging.basicConfig(filename='mylog.txt',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

driver_path='C:/Users/migue/PycharmProjects/chromedriver_win32/chromedriver.exe'
brave_path='C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'

option=webdriver.ChromeOptions()
option.binary_location=brave_path

browser=webdriver.Chrome(executable_path=driver_path,options=option)
browser.get('https://login.metafilter.com/')
user_name=browser.find_element_by_name('user_name')
user_name.send_keys('chavez24')

user_pass=browser.find_element_by_id('user_pass')
user_pass.send_keys('test25')
user_pass.submit()