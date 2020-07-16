from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/opt/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com/channel/UCmRFj7s3qBtadUujBd3Tujg")
subscriberCount = driver.find_element_by_id('subscriber-count')

print(subscriberCount.text)

# print(driver.page_source)

time.sleep(5)

driver.quit()