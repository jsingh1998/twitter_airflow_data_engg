import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

access_key = "4s1kQ41eGXjcxqKlMJNoUiYQy"
access_secret = "qVsZqsxSgnG3DZHEV4jyiJiFrGhJkB5wvIBOCVi0oM84zYKu1R"
consumer_key = "1673660379006656512-73XDNW9OhRExHleNybjaOVAbelSEOV"
consumer_secret = "HCs0H77e5ryA1ps21181tFZVJWbRLZXQezrsDSeS0FMH5"

# Twitter authentication
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

# Create an API object
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='@elonmusk', 
                            # 200 is the maximum allowed count
                            count=200,
                            include_rts = False,
                            # Necessary to keep full_text 
                            # otherwise only the first 140 words are extracted
                            tweet_mode = 'extended'
                            )

print(tweets)

