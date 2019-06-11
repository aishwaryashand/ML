#!/usr/bin/python3

import tweepy
from textblob  import TextBlob
import matplotlib.pyplot as plt

# making connection with twitter
# defining consumer key and secret
c_key="mB8A4V55vI5TQfi5DYTpE67AY"
c_sec="kQNdImsBEbYvWHx0PaEw6Xy4neTjcW4xtQQNxvn9NBdZidOFNb"

# to search & get inf you neeed to use token
# token key & secret
t_key="1003575775767846913-JwvqB6rnq9BecoNs3buryRN8XIPSpQ"
t_sec="yoajqEJnMIpTWqB4plMpLkMe8NRq1bzAOvHIAjHIQGSmr"

# connecting twitter API
auth_session=tweepy.OAuthHandler(c_key,c_sec)
# print(dir(auth_session))

# setting, sending token key & secret
auth_session.set_access_token(t_key,t_sec)

# now accessing API
api_connect=tweepy.API(auth_session)

# searching data
topic=api_connect.search('modi')
#print (topic)

for  i  in  topic:
    #  tokenized and clean   
    blob_data=TextBlob(i.text)
    # applying sentiment  output will be polarity 
print(blob_data.sentiment)

