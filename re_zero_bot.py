from dotenv import load_dotenv
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

#command to the bot tweet something. If fails, the output says: Algo falhou, burro.
try:
    tweet = client.create_tweet(text="teste")
    print(tweet)
except:
    print("Algo falhou, burro")