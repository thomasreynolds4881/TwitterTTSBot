from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
from datetime import datetime
import json
import keys
import config
import pyttsx3
import engineio
import sys

class TwitterStreamer():

	def __init__(self):
		pass

	def stream_tweets(self, filename, taglist, mode):
		#authenticate
		auth = OAuthHandler(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
		auth.set_access_token(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
		api = tweepy.API(auth)
		listener = StdOutListener(filename, api)
		
		#define a new Stream object; track is used for keyword search, follow for username search
		stream = Stream(auth, listener)
		if (mode == 0):
			userlist = []
			for i in taglist:
				userlist.append(str(api.get_user(screen_name = i).id)) #convert screenname into ID
			stream.filter(follow=userlist)
		elif (mode == 1):
			stream.filter(track=taglist)
		else: #if mode == 2
			stream.filter(locations=taglist)


class StdOutListener(StreamListener):

	def __init__(self, filename, api):
		self.filename = filename
		self.api = api

	def on_connect(self):
		print("Connected to server")
		pass
			
	def on_status(self, status):
		try:
			#determine if regular or extended tweet
			try:
				text = status.extended_tweet['full_text']
			except:
				text = status.text

			user = status.user.screen_name
			retweets = config.show_retweets
			engine = pyttsx3.init() #initialize TTS
			try:
				status.retweeted_status #check if status has retweeted_status; therefore, it's a retweet
				if (retweets == True):
					print("@"+user+": "+text)
					engine.say("New retweet from"+user)
					engine.say(text)
					engine.runAndWait()
					try:
						with open(self.filename, 'a') as tf:
							json.dump("@"+user+": "+text, tf)
							tf.write("\n")
					except:
						with open(self.filename, 'a') as tf:
							tf.write("Failed to write tweet\n")
				else:
					print("Retweet detected and skipped")
			except AttributeError as e:
				try:
					print("@"+user+" ("+status.place.name+"): "+text)
				except:
					print("@"+user+": "+text)
				
				engine.say("New tweet from "+user)
				engine.say(text)
				engine.runAndWait()
				try:
					with open(self.filename, 'a') as tf:
						json.dump("@"+user+": "+text, tf)
						tf.write("\n")
				except:
					with open(self.filename, 'a') as tf:
						tf.write("Failed to write tweet\n")
			return True
		except:
			return False

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
	elif (mode == 2):
		print("Using mode 2: filtering by location")
		taglist = config.location_list #for a location
	else:
		print("Error in config.py: mode doesn't exist")
		sys.exit()

	streamer = TwitterStreamer() #create a new streamer

	#Attempt to start and continue the twitter stream
	try:
		logdate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		print("Stream started:",logdate)
		with open(filename, 'a') as tf:
			tf.write("Stream started: "+logdate+"\n")
			tf.write("taglist: ")
			for i in taglist:
				tf.write("[")
				tf.write(str(i))
				tf.write("]")
			tf.write("\n")
		streamer.stream_tweets(filename, taglist, mode) #start streaming
		with open(filename, 'a') as tf:
			tf.write("Disconnecting\n\n")
		print("Disconnecting")

	#Shutdown if stream is interrupted or on a weird error
	except:
		with open(filename, 'a') as tf:
			tf.write("Disconnecting\n\n")
		print("Disconnecting")
		engine = pyttsx3.init()
		engine.say("Shutting down")
		engine.runAndWait()
		sys.exit()

main()
