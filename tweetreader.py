from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
import json
import keys
import config
import pyttsx3
import engineio

class TwitterStreamer():

	def __init__(self):
		pass

	def stream_tweets(self, filename, taglist, mode):
		listener = StdOutListener(filename)
		auth = OAuthHandler(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
		auth.set_access_token(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
		
		stream = Stream(auth, listener)
		if (mode == 1):
			stream.filter(track=taglist)
		else:
			stream.filter(follow=taglist)

class StdOutListener(StreamListener):

	def __init__(self, filename):
		self.filename = filename
			
	def on_data(self, data):
		retweets = config.show_retweets
		try:
			tweet = json.loads(data)
			text = json.dumps(tweet['text'])
			engine = pyttsx3.init()
			if (text):
				try:
					json.dumps(tweet['retweeted_status'])
					if (retweets == True):
						text = text[4:]
						print(text)
						say = "New retweeted post from"+text
						engine.say(say)
						engine.runAndWait()
						with open(self.filename, 'a') as tf:
							tf.write(text+"\n")
					else:
						print("Retweet detected and skipped")
				except:
					print(text)
					engine.say("New tweet:")
					engine.say(text)
					engine.runAndWait()
					with open(self.filename, 'a') as tf:
						tf.write(text+"\n")
			return True
		except:
			sys.exit()
		return True

	def on_error(self, status):
		print(status)
		sys.exit()

def main():
	filename = config.log_name
	mode = config.mode
	if (mode == 0):
		print("Using mode 0: filtering by account list")
		taglist = config.account_list #for an account
	elif (mode == 1):
		print("Using mode 1: filtering by phrase list")
		taglist = config.phrase_list #for a word
	else:
		print("Error in config.py: mode doesn't exist")
		sys.exit()

	streamer = TwitterStreamer()
	try:
		logdate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		print("Stream started:",logdate)
		print(taglist)
		with open(filename, 'a') as tf:
			tf.write("Stream started: "+logdate+"\n")
			tf.write("taglist: ")
			for i in taglist:
				tf.write("[")
				tf.write(i)
				tf.write("]")
			tf.write("\n")
		streamer.stream_tweets(filename, taglist, mode)
	except:
		engine = pyttsx3.init()
		engine.say("Critical error: halting program")
		engine.runAndWait()
		sys.exit()

main()