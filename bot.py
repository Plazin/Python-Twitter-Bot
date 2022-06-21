#import = importar uma biblioteca
#variável de ambiente virtual

from os import read, write
import tweepy #API do Twitter
import random #lib de random
import time # lib temporizador

# chaves para o bot funcionar na conta / env /melhorar o nome das chaves
api_key = ''
api_secret_key = '' 
access_key = ''
access_secret = ''
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def random_phrase():
    p1 = ['O confinamento', 'A Ciência', 'A OMS', 'A Universidade', 'A democracia', 'A vacina', 'O isolamento social', 'O racismo', 'O facismo'] # o assunto
    p2 = [' é uma invenção', ' é uma estratégia', ' é um plano', ' é uma conspiração', ' é uma mentira', ' é uma investida', ' é uma tentativa', ' é um delírio'] # o acontecimento
    p3 = [' da esquerda', ' da China', ' das FARC ',' do PT', ' do feminismo', ' da globo', ' dos gays', ' da foice de São Paulo'] # de onde
    p4 = [' para desmobilizar', ' para legimitar', ' para esconder', ' para destruir', ' para confundir', ' para intimidar', ' para ridicularizar', ' para atingir'] # pra que
    p5 = [' o Bolsonaro', ' o mito', ' a elite', ' as sociedades secretas', ' o elixir da vida', ' os repitilianos', ' a Terra Plana', ' o patriotismo', ' os evangélicos', ' a Bíblia'] # de quem
    genius_phrase = random.choice(p1) + random.choice(p2) + random.choice(p3) + random.choice(p4) + random.choice(p5)
    return genius_phrase 

def _main_():
    read_last_seen_str = str(read_last_seen(FILE_NAME))
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode = 'extended')
    print('Ultimo ID pesquisado:' + read_last_seen_str)
    for tweet in reversed(tweets):
        store_last_seen(FILE_NAME, tweet.id)
        genius_phrase = random_phrase()
        api.update_status('@'+ tweet.user.screen_name + ' ' + genius_phrase, in_reply_to_status_id=tweet.id)

while True:
    _main_()
    time.sleep(60)
