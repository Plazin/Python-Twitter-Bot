from dotenv import load_dotenv
import random
import time
import dotenv
import tweepy
import os
load_dotenv()

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

client = tweepy.Client(consumer_key=consumer_key,consumer_secret=consumer_secret,access_token=access_token,access_token_secret=access_token_secret)

def random_phrases():
    list1 = ['O Retorno pela Morte ','A Seleção Real ','O Loop Temporal ','O Culto da Bruxa ','O Santuário ','Rota Alternativa ','A Guilda dos Assassinos ','A Torre das Pleiades ']
    list2 = ['é uma invenção ','é uma criação ','é uma estratégia ','é uma mentira ','é um delírio ','é uma loucura ','é uma conspiração ','é uma tentativa ']
    list3 = ['do Hoshin ', 'do Flugel ','da Satella ', 'da Echidna ', 'do Volcanica ','do Reid Astrea ','do『Natsuki Subaru』','do Tappei ']
    list4 = ['pra esconder ','pra destruir ','pra confundir ','pra atingir ','pra ridicularizar ','pra comer ','pra estourar ','pra enganar ']
    list5 = ['o Subaru.','a Rem.', 'a Ram.', 'o Aldebaran.','o Roswaal.','a Minerva.','o Otto.','a Priscilla.']
    random_moment = random.choice(list1) + random.choice(list2) + random.choice(list3) + random.choice(list4) + random.choice(list5)
    return random_moment

#command to the bot tweet something. If fails, the output says: Algo falhou, burro.
def _main_():
    randomium = random_phrases()
    try:
        random_tweet = client.create_tweet(text=randomium)
        print(random_tweet)
        return random_tweet
    except:
        print("algo falhou")

while True:
    _main_()
    time.sleep(120)