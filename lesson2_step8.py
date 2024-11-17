import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os 

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/file_input.html"
browser.get(link)

input1 = browser.find_element(By.NAME, "firstname")
input1.send_keys('Sergey')

input2 = browser.find_element(By.NAME, "lastname")
input2.send_keys('Petrov')


input3 = browser.find_element(By.NAME, "email")
input3.send_keys('test@mail.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt') 

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt') 

input4 = browser.find_element(By.ID, "file")
input4.send_keys(file_path)

input5 = browser.find_element(By.CSS_SELECTOR, "button.btn")
input5.click()


time.sleep(10)

browser.quit()
