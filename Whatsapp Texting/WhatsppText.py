from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

browser = webdriver.Chrome("D:\PRACTISE CODE\Python Practise\Whatspp Access Texter\chromedriver.exe") #update driver according to your chrome version, or else it will not run
browser.get('http://web.whatsapp.com')
wait = WebDriverWait(browser, 60)

target = '"safin"'  # senders name // for user input , input("Type the target name")
string = " egulai automation B) "  # message that will send // for user input of text message , input("Type the message you want to send")
x_arg = '//span[contains(@title,' + target + ')]'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()

input_box = browser.find_elements_by_class_name('_2_1wd')[1] #for multiple class name sharing the same name, [1] is the index number,for single class name, find_Element_By_Class_Name
for i in range(173):
    input_box.send_keys(str(i) + string + Keys.ENTER)

# Audio file send

# attachment_section = browser.find_element_by_xpath('//div[@title= "Attach"]') #searching attachment section in chat
# attachment_section.click()
#
# audio_file= browser.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')  # search image add button
# audio_file.send_keys('C:/Users/ASUS-PC/Downloads/Music/Imagine Dragons - Bad Liar.mp3') #adding image path // for user input path, input('Please enter the file path')
#
# sleep(3)
# send_button  = browser.find_element_by_xpath('//span[@data-icon="send"]')
# send_button.click()


# Image send

# attachment_section = browser.find_element_by_xpath('//div[@title= "Attach"]') #searching attachment section in chat
# attachment_section.click()
#
# image_file= browser.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')  # search image add button
# image_file.send_keys('C:/Users/ASUS-PC/Downloads/images.jpg') #adding image path // for user input path, input('Please enter the file path')
#
# sleep(3)
# send_button  = browser.find_element_by_xpath('//span[@data-icon="send"]')
# send_button.click()
