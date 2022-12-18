import sys
import time
import simple_twit
import random


CONSUMER_KEY = 
CONSUMER_SECRET = 


def twitterbot(api): # unicode encoding for an emoji
    simple_twit.send_tweet(api, "Emoji Twitter Bot")
    emoji_list = ['\U0001f47b', '\U0001f916', '\U0001f47d', '\U0001f47e',
                  '\U0001f4A3', '\U0001f476', '\U0001f9d4']
    emoji_string = "I am a(n):  " + random.choice(emoji_list)
    time_string = "Seconds since the epoch: " + str(int(time.time()))
    tweet_string = emoji_string + "\n" + time_string
    result = simple_twit.send_tweet(api, tweet_string)
    print(result.id)
    print(result.text)
    print()


if __name__ == "__main__":
    simple_twit.version()
    api = simple_twit.create_api(CONSUMER_KEY, CONSUMER_SECRET)


    twitterbot(api)
