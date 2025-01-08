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
    input_element.send_keys("Murillo")

# COMPETITION
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

# DADOS DE SCOUT

scout_new = {}

sleep(10)

blocks = driver.find_elements(By.CSS_SELECTOR,"div[class='Box Flex VhXzF kGBmhP']")

if len(blocks) < 2:
    sleep(40)
    blocks = driver.find_elements(By.CSS_SELECTOR,"div[class='Box Flex VhXzF kGBmhP']")

blocks_scout = blocks[1].find_elements(By.CSS_SELECTOR,"div[class='Box jfMEge']")



n = 0
for i,bl in enumerate(blocks_scout):
    if i < 2:
        continue    
    texto = bl.text.split("\n")[1:]
    result = {texto[n]: texto[n + 1] for n in range(0, len(texto), 2)}
    print(result)
    scout_new.update(result)

profile = {'profile': ""}


try:
    profile['profile'] = driver.find_element(
        By.CLASS_NAME,"bFoDOL").get_attribute("src")
except NoSuchElementException:
    print("exception")
    sleep(10)
    profile['profile'] = driver.find_element(
        By.CLASS_NAME,"bFoDOL").get_attribute("src")


team_info = {}
player_info = {}

team_element = driver.find_element(By.CSS_SELECTOR,"div[class='Box Flex bsXxAs jLRkRA']")

team_info['name_team'] = team_element.find_element(By.CSS_SELECTOR,"div[class='Text leMLNz']").text
team_info['img_team'] = team_element.find_element(By.TAG_NAME,"img").get_attribute("src")

player_element = driver.find_element(By.CSS_SELECTOR,"div[class='Box Flex ggRYVx flkZQO']")

scout_new.update(team_info)
scout_new.update(profile)

print(scout_new)


sleep(10)

driver.quit()


