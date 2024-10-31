from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver.find_elementnt(By.CSS_SELECTOR, '<** Selector 복붙 **>').click()
tine.sleep(1)

driver.find_elementnt(By.CSS_SELECTOR, '<** Selector 복붙 **>').click()
tine.sleep(3)

news_titles = driver.find_elements(By.CSS_SELECTOR. ".news_tit")
print(news_titles)

for i in news_titles :
    title = i.text
    href = i.get_attribute('href')
    print(title , " : ", href)