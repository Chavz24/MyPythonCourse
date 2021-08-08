#abre el brave browser en https://inventwithpython.com, busca un elemento y hace click en un botton

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
browser.get('https://inventwithpython.com')

try:
    elem=browser.find_element_by_class_name('cover-thumb')
    print('Found <%s> whit that class name' %(elem.tag_name))
except:
    print('Nada')

link_elem=browser.find_element_by_link_text('Read Online for Free')
link_elem.click()