from dotenv import load_dotenv
import random
import time
import dotenv
from tweepy import (Client,API,Media)
import os
import requests
from PIL import Image
load_dotenv()

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
auth = os.getenv("ACCESS_TOKEN_SECRET")

client = Client(consumer_key=consumer_key,consumer_secret=consumer_secret,access_token=access_token,access_token_secret=access_token_secret)
media = API(auth=auth)
supermedia = Media(auth=auth)

#function with arrays that conteins all phrases that can be used to create a randomic tweet
def random_phrases():
    list1 = ['O Retorno pela Morte ','A Seleção Real ','O Loop Temporal ','O Culto da Bruxa ','O Santuário ','A Rota da Preguiça ','A Guilda dos Assassinos ','A Torre das Pleiades ',
    'A Rota da Ganância ','A Rota do Orgulho ','A Rota da Ira ','A Rota da Inveja ','A Rota da Vingança ','A Rota da Luxúria ','A Rota da Gula ','A Rota Escolar ','O Rinha IF '
    'O canal do Barusu ','O canal do Culto das Bruxas ','O canal do Zenny ','O canal do Zas ']

    list2 = ['é uma invenção ','é uma criação ','é uma estratégia ','é uma mentira ','é um delírio ','é uma loucura ','é uma conspiração ','é uma tentativa ','é uma uma paranóia ',
    'é uma alternativa ']

    list3 = ['do Hoshin ', 'do Flugel ','da Satella ', 'da Echidna ', 'do Volcanica ','do Reid Astrea ','do『Natsuki Subaru』','do Tappei ','do Barusu ','do Culto das Bruxas ',
    'da Subaru ','da Daphne ','da Sekhmet ','do Puck ','da Ram ','da Felt ','da Priscilla ','da Anastasia ','da Crusch ','do Reinhard ','do Felix ','do Julius ','do Roswaal ',
    'do Garfiel ','da Frederica ','do Schult ','da Patrasche ','do Otto ','do véio Rom','do Ricardo ','do Ricardo (clone) ','da Mimi ','do Hetaro ','do Tivey ','do Willhelm ','da Carmilla ',
    'da Typhon ','da Pandora ','do Regulus ','do Ley Batenkaitos ','da Sirius ','da Capella ','da Elsa ','do Stride ','do Kadomon ','da Petra ','Russell Fellow ']

    list4 = ['pra esconder ','pra destruir ','pra confundir ','pra atingir ','pra ridicularizar ','pra comer ','pra estourar ','pra enganar ','pra roubar ']

    list5 = ['o Subaru.','a Rem.', 'a Ram.', 'o Aldebaran.','o Roswaal.','a Minerva.','o Otto.','a Priscilla.','a comunidade de Re:Zero.','o Hoshin.', 'o Flugel.','a Satella.', 
    'a Echidna.', 'o Volcanica.','o Reid Astrea.','o『Natsuki Subaru』.','o Tappei.','o Barusu do Youtube.','o Culto das Bruxas do Youtube.',
    'a Subaru.','a Daphne.','a Sekhmet.','o Puck.','a Ram.','a Felt.','a Priscilla.','a Anastasia.','a Crusch.','o Reinhard.','o Felix.','o Julius.','o Roswaal.',
    'o Garfiel.','a Frederica.','o Schult.','a Patrasche.','o Otto.','o véio Rom.','o Ricardo.','do Ricardo (clone)','a Mimi.','o Hetaro.','o Tivey.','o Willhelm.','a Carmilla.',
    'a Typhon.','a Pandora.','o Regulus.','o Ley Batenkaitos.','a Sirius.','a Capella.','a Elsa.','o Stride.','o Kadomon.','a Petra.','o Russell Fellow.']

    random_moment = random.choice(list1) + random.choice(list2) + random.choice(list3) + random.choice(list4) + random.choice(list5)
    return random_moment

#function with arrays that conteins all images that can be used to create a randomic tweet
#def random_images():

#    image_list1 = ('/susbaru.jpg')
#    image_list2 = ('/echidna.png')

#    random_person = random.choice(image_list1)
#    return random_person

def upload_media(text, filename):
    image_media = media.media_upload(filename)
    media.update_status(text, media_ids = [media.media_id_string])
    return image_media

#command to the bot tweet something. If fails, the output says: Algo falhou.
def _main_():
    #randomium_img = random_images()
    randomium = random_phrases()
    try:
        #random_tweet_img = media.update_status_with_media(filename=randomium_img) #usar o simple_upload, junto com media_ids, apontado.
        random_tweet = client.create_tweet(text=randomium)
        print(random_tweet)
        return random_tweet
    except:
        print("algo falhou")

while True:
    _main_()
    time.sleep(120)