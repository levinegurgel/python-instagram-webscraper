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
print('Número de inscritos: ' + subscriberCount.text.replace(' subscribers', ''))

time.sleep(3)
driver.execute_script("window.scrollTo(0, 1680)") 
time.sleep(2)
link = driver.find_element_by_link_text("Panelaço com João Gordo - Peixe de tofu com Mano Brown")
link.click()

try:
    time.sleep(6)
    skipButton = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ytp-ad-skip-button"))
    )
finally:
    time.sleep(6)
    skipButton = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ytp-ad-skip-button"))
    )

skipButton.click()

view_num = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "view-count"))
)

print('Número de visualizações: ' + view_num.text.replace(' views', ''))

time.sleep(5)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# driver.execute_script("window.scrollTo(0, 1680)") 
# driver.sendKeys(Keys.PAGE_DOWN)
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)

time.sleep(5)

commentCount = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "ytd-comments-header-renderer"))
)

print('Número de comentários: ' + commentCount.text.replace(u'Comments', ''))
driver.quit()