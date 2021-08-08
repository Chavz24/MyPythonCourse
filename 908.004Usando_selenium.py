#abre elbrave browser en el buscardor duck y  escribe hola mundo y presona enter

import logging
from selenium import webdriver
from  selenium.webdriver.common.keys import Keys


open('mylog.txt', 'w').write('\n')
logging.basicConfig(filename='mylog.txt',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)




dirver_path='C:/Users/migue/PycharmProjects/chromedriver_win32/chromedriver.exe'

brave_path='C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'

option=webdriver.ChromeOptions()
option.binary_location=brave_path


browser=webdriver.Chrome(executable_path=dirver_path,options=option)
browser.get('https://duckduckgo.com/?t=brave')
search_bar=browser.find_element_by_id('search_form_input_homepage')
search_bar.clear()
search_bar.send_keys("Hola Mundo")
search_bar.send_keys(Keys.RETURN)
browser.close()


logging.debug(f'{type(browser)}')







