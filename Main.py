from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

browser= webdriver.Chrome("D:\PRACTISE CODE\Python Practise\Whatspp Access Texter\chromedriver.exe")
browser.get("https://www.youtube.com")
message= browser.find_element_by_link_text("Trending")
message.click()
#wait= WebDriverWait(browser,2000)
sleep(3)

search= browser.find_element_by_name('search_query')
search.send_keys('purple lamborghini')
button=browser.find_element_by_id('search-icon-legacy')
button.click()

sleep(3)

#play = browser.find_elements_by_partial_link_text('Skrillex & Rick Ross - Purple Lamborghini [Official Video]')
play=browser.find_element_by_xpath('//div[@class="text-wrapper style-scope ytd-video-renderer"]')
play.click()

sleep(12)
browser.close()