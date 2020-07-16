from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/opt/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)

#panelaço
driver.get("https://www.youtube.com/channel/UCmRFj7s3qBtadUujBd3Tujg")
subscriberCount = driver.find_element_by_id('subscriber-count')
print(subscriberCount.text)

time.sleep(5)

link = driver.find_element_by_link_text("Panelaço com João Gordo - Peixe de tofu com Mano Brown")
link.click()

view_num = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "view-count"))
)

print('Número de visualizações: ' + view_num.text.replace(' views', ''))

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "comment-section-header-renderer")))
    for comment_num in driver.find_elements_by_class_name("comment-section-header-renderer"):
        print('Número de comentários: ' + comment_num.text.replace(u'COMMENTS • ', ''))
finally:
    driver.quit()

#Envios mais famosos
# ytp-ad-skip-button ytp-button
# print(driver.page_source)


# driver.quit()