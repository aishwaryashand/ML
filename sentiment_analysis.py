#!usr/bin/python3

# a class to preprocess all the tweets, both the test and training data
# wel will use regular expressionand NLTK for preprocessing

import re
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords

class PreProcessTweets:
	def _init_(self):
		self._stopwords=set(stopwords.words('english')+list(punctuation)+['AT_USER','URL'])

	def processTweets(self,list_of_tweets):
		# the list of tweets is a list of dictionaries which should have the keys, text and label
		processedTweets=[]
		# this list will be a list of tuples. each tuple is a tweet which is a list of words and its label
		for tweet in list_of_tweets:
		 processedTweets.append((self._processtweet(tweet["text"]),tweet["label"]))
		return processedTweets

	def _processedTweets(self,tweet):
	 # conver to lower case
	 tweet=tweet.lower()
	 # replace links with the word URL
	 tweer=re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
	 # replace @username with "AT_USER"
	 tweet=re.sub('@[^\s]+','AT_USER',tweet)
	 # replace #word with word
	 tweet=re.sub(r'#([^\s]+)',r'\1',tweet)
	 
	 tweet=word_tokenize(tweet)
	 # this tokenizes the tweet into a list of words
	 # let's now return this list minus stopwords
	 return [word for word in tweet if word not in self._stopwords]

tweetProcessor=PreProcessTweets()
ppTrainingData=tweetProcessor.processTweets(trainingData)
ppTestData=tweetProcessor.processTweets(testData)

ppTrainingData[:5]
