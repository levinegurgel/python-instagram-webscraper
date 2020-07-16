from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/home/levine/Softwares/google/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com/channel/UCtkaKWXdSleRU3azAeBRrmg")

# search = driver.find_element_by_name("search_query")
# search.send_keys("test")
# search.sed_keys(Keys.RETURN)

subscriberCount = driver.find_element_by_id('subscriber-count')

print(subscriberCount.text)

# print(driver.page_source)

time.sleep(5)

driver.quit()