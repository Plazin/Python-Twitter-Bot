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
    list1 = ['O Retorno pela Morte ','A Seleção Real ','O Loop Temporal ','O Culto da Bruxa ','O Santuário ','Rota da Preguiça ','A Guilda dos Assassinos ','A Torre das Pleiades ',
    'A Rota da Ganância ','A Rota do Orgulho ','A Rota da Ira ','A Rota da Inveja ','A Rota da Vingança ','A Rota da Luxúria ','A Rota da Gula  ','A Rota Escolar ','O Rinha IF '
    'O canal do Barusu ','O canal do Culto das Bruxas ','O canal do Zenny ','O canal do Zas ']

    list2 = ['é uma invenção ','é uma criação ','é uma estratégia ','é uma mentira ','é um delírio ','é uma loucura ','é uma conspiração ','é uma tentativa ','é uma uma paranóia',
    'é uma alternativa ']

    list3 = ['do Hoshin ', 'do Flugel ','da Satella ', 'da Echidna ', 'do Volcanica ','do Reid Astrea ','do『Natsuki Subaru』','do Tappei ','do Barusu ','do Culto das Bruxas ',
    'da Subaru ','da Daphne ','da Sekhmet ','do Puck ','da Ram ','da Felt ','da Priscilla ','da Anastasia ','da Crusch ','do Reinhard ','do Felix ','do Julius ','do Roswaal ',
    'do Garfiel ','da Frederica ','do Schult ','da Patrasche ','do Otto ','do véio Rom','do Ricardo ','do Ricardo (clone)','da Mimi ','do Hetaro ','do Tivey ','do Willhelm ','da Carmilla ',
    'da Typhon ','da Pandora ','do Regulus ','do Ley Batenkaitos ','da Sirius ','da Capella ','da Elsa ','do Stride ','do Kadomon ','da Petra ','Russell Fellow ']

    list4 = ['pra esconder ','pra destruir ','pra confundir ','pra atingir ','pra ridicularizar ','pra comer ','pra estourar ','pra enganar ','pra roubar ']

    list5 = ['o Subaru.','a Rem.', 'a Ram.', 'o Aldebaran.','o Roswaal.','a Minerva.','o Otto.','a Priscilla.','a comunidade de Re:Zero.','o Hoshin.', 'o Flugel.','a Satella.', 
    'a Echidna.', 'o Volcanica.','o Reid Astrea.','o『Natsuki Subaru』.','o Tappei.','o Barusu do Youtube.','o Culto das Bruxas do Youtube.',
    'a Subaru.','a Daphne.','a Sekhmet.','o Puck.','a Ram.','a Felt.','a Priscilla.','a Anastasia.','a Crusch.','o Reinhard.','o Felix.','o Julius.','o Roswaal.',
    'o Garfiel.','a Frederica.','o Schult.','a Patrasche.','o Otto.','o véio Rom.','o Ricardo.','do Ricardo (clone)','a Mimi.','o Hetaro.','o Tivey.','o Willhelm.','a Carmilla.',
    'a Typhon.','a Pandora.','o Regulus.','o Ley Batenkaitos.','a Sirius.','a Capella.','a Elsa.','o Stride.','o Kadomon.','a Petra.','o Russell Fellow.']

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
    time.sleep(10)