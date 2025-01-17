from selenium import webdriver
from selenium.webdriver.chrome.service import  Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from .find_similar_string import find_similar_string
from time import sleep
import re

empty_obj = ['liga', 'temp', 'Total_played', 'Started', 'Minutes_per_game', 'Total_minutes_played', 'Team_of_the_week', 'Goals', 'Expected_Goals_(xG)', 'Scoring_frequency', 'Goals_per_game', 'Shots_per_game', 'Shots_on_target_per_game', 'Big_chances_missed', 'Goal_conversion', 'Penalty_goals', 'Penalty_conversion', 'Free_kick_goals', 'Free_kick_conversion', 'Goals_from_inside_the_box', 'Goals_from_outside_the_box', 'Headed_goals', 'Left_foot_goals', 'Right_foot_goals', 'Penalty_won', 'Assists', 'Expected_Assists_(xA)', 'Touches', 'Big_chances_created', 'Key_passes', 'Accurate_per_game', 'Acc._own_half', 'Acc._opposition_half', 'Acc._long_balls', 'Acc._chipped_passes', 'Acc._crosses', 'Interceptions_per_game', 'Tackles_per_game', 'Possession_won', 'Balls_recovered_per_game', 'Dribbled_past_per_game', 'Clearances_per_game', 'Error_led_to_shot', 'Error_led_to_goal', 'Penalties_committed', 'Succ._dribbles', 'Total_duels_won', 'Ground_duels_won', 'Aerial_duels_won', 'Possession_lost', 'Fouls', 'Was_fouled', 'Offsides', 'Yellow', 'Yellow-Red', 'Red_cards', 'nacionalidade', 'nascimento', 'altura', 'pé', 'pos', 'Name', 'name_team', 'img_team', 'profile', 'data', 'escudo_mandante', 'escudo_visitante', 'placar_mandante', 'placar_visitante', 'nome_mandante', 'nome_visitante', 'positions']

def replace_spaces_in_keys(obj):
    new_obj = {}
    for key, value in obj.items():
        new_key = re.sub(r'\s+', '_', key)
        new_obj[new_key] = value
    return new_obj

def scrape_data(data,competicao=None):

    ano = ""
    if competicao:
       for n in competicao.split(" "):
           if n[:2].isdigit():
               ano = n
               
            
    service = Service(executable_path="drivers/chromedriver.exe")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=service,options=chrome_options)

    driver.get("https://www.sofascore.com")
    driver.maximize_window()

    input_element = driver.find_element(By.ID,"search-input")

    if input_element.is_displayed():
        input_element.send_keys(data)
        sleep(5)
        button = [el for el in driver.find_elements(By.CLASS_NAME,"Chip") if el.text == "Player"][0]
        sleep(5)
        button.click()
        sleep(5)

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

    # AQUI ESCOLHE A COMPETICAO
    btn_element = ""
    if competicao is not None:
        ### VAI CLICAR NO PRIMEIRO BOTÃO DE COMPETIÇÃO
        try:
            sleep(20)
            btn_element = driver.find_elements(By.CSS_SELECTOR,"button[class='DropdownButton jQruaf']")
            if len(btn_element) == 2:
                btn_element = btn_element[0]
            else:
                btn_element = btn_element[1]
            if btn_element.is_displayed():
                btn_element.click()
        except:
            ...
        #MELHOR UTILIZAR SETAS MESMO
        n = 0
        arr_ligas = []
        sleep(5)
        while n < 20:
            if btn_element.text not in arr_ligas:
                arr_ligas.append(btn_element.text)
            btn_element.send_keys(Keys.ARROW_DOWN)
            sleep(5)
            btn_element.send_keys(Keys.ENTER)
            sleep(5)
            btn_element.send_keys(Keys.ENTER)
            n += 1
    
    if competicao:    
        COMPETICAO = find_similar_string(competicao,arr_ligas)
    if competicao:
        n = 0
        sleep(5)
        while n < 20:
                if btn_element.text == COMPETICAO:
                    break
                sleep(5)
                btn_element.send_keys(Keys.ARROW_DOWN)
                sleep(5)
                btn_element.send_keys(Keys.ENTER)
                sleep(5)
                btn_element.send_keys(Keys.ENTER)
                n += 1

    sleep(20)
    btn_season = driver.find_elements(By.CSS_SELECTOR,"button[class='DropdownButton jQruaf']")[-1]
    if ano: 
        #ESCOLHER TEMPORADA
        sleep(10)
        driver.execute_script("""
        const buttons = document.querySelectorAll('button.DropdownButton.jQruaf');
        if (buttons.length > 0) {
            buttons[buttons.length - 1].click();
        }
        """)    

        sleep(3)
        n = 0 
        if ano:
            ano_new = ano if len(ano) > 2 else f"20{ano}"
            while n < 20:
                if btn_season.text == ano_new:
                    break
                sleep(7)
                btn_season.send_keys(Keys.ARROW_DOWN)
                sleep(7)
                btn_season.send_keys(Keys.ENTER)
                sleep(7)
                btn_season.send_keys(Keys.ENTER)
                n += 1

    # DADOS DE SCOUT
    scout_new = {}

    info_liga = {}

    sleep(5)
    try:
        nome_liga = driver.find_element(By.CSS_SELECTOR,f"bdi[class='Text kCBySt']").text
        info_liga['liga'] = nome_liga
    except NoSuchElementException:
         sleep(5)
         nome_liga = driver.find_element(By.CSS_SELECTOR,f"bdi[class='Text kCBySt']").text
         info_liga['liga'] = nome_liga
    except:
        sleep(5)
        btn_element.click()
        nome_liga = driver.find_element(By.CSS_SELECTOR,f"bdi[class='Text kCBySt']").text
        info_liga['liga'] = nome_liga
        
    temp_liga = btn_season.find_element(By.CSS_SELECTOR,"bdi[class='Text jFxLbA']").text
    info_liga['temp'] = temp_liga

    scout_new.update(info_liga)


    sleep(10)

    try:
        blocks = driver.find_element(By.CSS_SELECTOR,"div[class='Box kUNcqi sc-91097bb0-2 jwUHH']")
    except IndexError:
        sleep(10)
        blocks = driver.find_element(By.CSS_SELECTOR,"div[class='Box kUNcqi sc-91097bb0-2 jwUHH']")

    
    blocks_scout = blocks.find_elements(By.CSS_SELECTOR,"div[class='Box jfMEge']")

    for i,bl in enumerate(blocks_scout):
        if i < 2:
            continue    
        texto = bl.text.split("\n")[1:]
        result = {texto[n]: texto[n + 1] for n in range(0, len(texto), 2)}
        scout_new.update(result)

    profile = {'profile': ""}


    try:
        profile['profile'] = driver.find_element(
            By.CLASS_NAME,"bFoDOL").get_attribute("src")
    except NoSuchElementException:
        sleep(10)
        profile['profile'] = driver.find_element(
            By.CLASS_NAME,"bFoDOL").get_attribute("src")


    team_info = {}
    try:
        team_element = driver.find_element(By.CSS_SELECTOR,"div[class='Box Flex bsXxAs jLRkRA']")

        team_info['name_team'] = team_element.find_element(By.CSS_SELECTOR,"div[class='Text leMLNz']").text
        team_info['img_team'] = team_element.find_element(By.TAG_NAME,"img").get_attribute("src")
    except NoSuchElementException:
        team_info['team_info'] = 'Sem Clube'

    player_element_status = driver.find_elements(By.CSS_SELECTOR,"div[class='Box gsaNZo']")

    player_attributes = {}

    player_attributes['bandeira'] = player_element_status[0].find_element(By.TAG_NAME,"img").get_attribute("src")
    player_attributes['nacionalidade'] = player_element_status[0].text.split("\n")[1]
    player_attributes['idade'] = player_element_status[1].text.split("\n")[1]
    player_attributes['nascimento'] = player_element_status[1].text.split("\n")[0]
    player_attributes['altura'] = player_element_status[2].text.split("\n")[1].split(" ")[0]
    player_attributes['pé'] = player_element_status[3].text.split("\n")[1]
    player_attributes['pos'] = driver.find_element(By.CSS_SELECTOR,"div[class='Box oWZdE']").text.split("\n")[1]
    player_attributes['Name'] = driver.find_element(By.CSS_SELECTOR,"h2[class='Text cuNqBu']").text

    
    scout_new.update(player_attributes)
    scout_new.update(team_info)
    scout_new.update(profile)

    partida = {}
    
    try:
        data_ultimo_jogo = driver.find_element(By.CSS_SELECTOR,"span[class='Text hZKSbA']")

        partida['data'] = data_ultimo_jogo.text.split(":")[0][0:-2]

        resultado_ultimo_jogo = driver.find_element(By.CSS_SELECTOR,"div[class='Box Flex dZNeJi bnpRyo']")

        escudos_dos_times = resultado_ultimo_jogo.find_elements(By.TAG_NAME,"img")

        partida['escudo_mandante'] = escudos_dos_times[0].get_attribute("src")
        partida['escudo_visitante'] = escudos_dos_times[1].get_attribute("src")

        placar = resultado_ultimo_jogo.find_element(By.CSS_SELECTOR,"div[class='Box iCtkKe']").text.strip().split("-") 
        nome_dos_times = resultado_ultimo_jogo.find_elements(By.CSS_SELECTOR,"bdi[class='Text fIvzGZ']")


        partida['placar_mandante'] = placar[0]
        partida['placar_visitante'] = placar[1]

        partida['nome_mandante'] = nome_dos_times[0].text
        partida['nome_visitante'] = nome_dos_times[1].text

        scout_new.update(partida)
       
    except Exception:
        block_prox_partida = driver.find_elements(By.CSS_SELECTOR,"div[class='Box lfqAOf']")
        partida['nome_mandante'] = block_prox_partida[0].find_element(By.TAG_NAME,"bdi").text
        partida['nome_visitante'] = block_prox_partida[1].find_element(By.TAG_NAME,"bdi").text

        partida['escudo_mandante'] = block_prox_partida[0].find_element(By.TAG_NAME,"img").get_attribute("src")
        partida['escudo_visitante'] = block_prox_partida[1].find_element(By.TAG_NAME,"img").get_attribute("src")

        partida['data'] = driver.find_element(By.CSS_SELECTOR,"div[class='Box dUMdHh']").text.replace("\n"," ")
        
        scout_new.update(partida)



    # PEGA POSIÇÃO DO JOGADOR
    element_field_pos = driver.find_element(By.CSS_SELECTOR,"div[class='Box Flex evCGta eCIOYr']")
    positions = element_field_pos.find_elements(By.TAG_NAME,"text")

    if positions:
        scout_new['positions'] = []

        for pos in positions:
            scout_new['positions'].append(pos.text)

    scout_final = replace_spaces_in_keys(scout_new)
    for field in empty_obj:
        if field not in scout_final:
            scout_final[field] = f"N/A" 

    driver.quit()

    return scout_final


