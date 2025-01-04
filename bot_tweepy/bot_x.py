import tweepy as tw
import os
from dotenv import load_dotenv

load_dotenv("../.env")

BEARER_TOKEN = os.getenv('BEARER_TOKEN')
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')


def bot_buscar(bd):
    lista_antiga = bd
    lista = []
    
    client = tw.Client(bearer_token=BEARER_TOKEN,consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET)

    response = client.search_recent_tweets(query="@DataScoutBR")
    if response.data:
        for tweet in response.data:
            if tweet.id in lista_antiga:
                continue
            # AQUI VAI O CODIGO
            lista.append(tweet.id)
        
    lista = [*lista_antiga,*lista]
    

    return lista


# client.create_tweet(text='Teste')