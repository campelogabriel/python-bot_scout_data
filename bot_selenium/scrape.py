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

btn = driver.find_elements(By.CSS_SELECTOR,"div[class='Dropdown gSFIyj']")

for i,n in enumerate(btn):
   if i == 1:
       n.click()


# AQUI ESCOLHE A COMPETICAO

COMPETITION = "Carioca"

competition_btns = driver.find_elements(By.CLASS_NAME,"jFxLbA")

# for btn in competition_btns:
#     if COMPETITION in btn.text:
#         btn.click()


# DADOS DE SCOUT

scout_new = {}

sleep(20)

blocks = driver.find_elements(By.CSS_SELECTOR,"div[class='Box Flex VhXzF kGBmhP']")[1]
blocks_scout = blocks.find_elements(By.CSS_SELECTOR,"div[class='Box jfMEge']")

n = 0
for i,bl in enumerate(blocks_scout):
    if i < 2:
        continue    
    texto = bl.text.split("\n")[1:]
    result = {texto[n]: texto[n + 1] for n in range(0, len(texto), 2)}
    scout_new.update(result)

print(scout_new)

sleep(60)

driver.quit()


