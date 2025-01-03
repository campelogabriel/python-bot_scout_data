from selenium import webdriver
from selenium.webdriver.chrome.service import  Service 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from time import sleep

service = Service(executable_path="drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.sofascore.com/")

driver.maximize_window()

input_element = driver.find_element(By.ID,"search-input")

if input_element.is_displayed():
    input_element.send_keys("paulinho paula")


try:
    btn_element = driver.find_element(By.CLASS_NAME,"sc-44409fa7-0")
    if btn_element.is_displayed():
        btn_element.click()
except NoSuchElementException:
    sleep(5)
    btn_element = driver.find_element(By.CLASS_NAME,"sc-44409fa7-0")
    if btn_element.is_displayed():
        btn_element.click()
except StaleElementReferenceException:
    sleep(5)
    btn_element = driver.find_element(By.CLASS_NAME,"sc-44409fa7-0")
    if btn_element.is_displayed():
        btn_element.click()

sleep(15)

btn = driver.find_elements(By.CLASS_NAME,"jQruaf")

for i,n in enumerate(btn):
   if i == 1:
       n.click()


# COMPETITION = "Carioca"

# competition_btns = driver.find_elements(By.CLASS_NAME,"jFxLbA")

# print(competition_btns)

# for btn in competition_btns:
#     if COMPETITION in btn.text:
#         btn.click()


sleep(60)

driver.quit()


