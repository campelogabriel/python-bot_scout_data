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

scout_partidas = {
    "partidas_jogadas": 0,
    "minutagem": 0,
}
scout_ataque = {
    "gols":0,
    "xG" : 0.0,
    "chutes_por_jogo": 0.0,
    "chutes_no_alvo": 0.0,
    "grandes_chances_perdidas":0,
}
scout_passes = {
    "assistencias":0,
    "xA": 0.0,
    "grandes_chances_criadas": 0,
    "acerto_no_passe" : "0%",
    "acerto_na_bola_longa": "0%"
}

scout_defesas = {
    "interpcoes_por_jogo" : 0.0,
    "bolas_recuperdas_por_jogo": 0.0,
    "desarmes_por_jogo" : 0.0,
    "dribles_sofridos_por_jogo": 0.0,
    "erros_que_levaram_ao_chute": 0,
    "errors_que_levaram_ao_gol": 0
}
scout_outros = {
    "sucesso_nos_dribles" : "0%",
    "duelos_vencidos": "0%",
    "duelos_no_chão_vencidos": "0%",
    "duelos_aereos_vencidos": "0%",
    "posse_perdida": 0.0
}

sleep(13)

blocks = driver.find_elements(By.CSS_SELECTOR,"div[class='Box Flex VhXzF kGBmhP']")[1]

blocks_scout = blocks.find_elements(By.CSS_SELECTOR,"div[class='Box jfMEge']")
for i,bl in enumerate(blocks_scout):

    if i < 2:
        continue    
    print("*********** ", i)
    print(bl.text)

sleep(60)

driver.quit()


