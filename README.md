A Twitter bot that fetches tweets via keyword or account number, and then reads them out via Text-To-Speech. This is one of my first attempts at a solo project; if you have any feedback feel free to send me a message on reddit (u/CustomCuber).

# Files
* tweetreader.py: runs the tweet streamer
* config.py: used to change streaming settings
* keys.py: location to put Twitter app access keys
* tweetlog.json: log file

# Libraries
* Tweepy: streams tweets
* pyttsx3: used for tts

# References
* [LucidProgramming](https://www.youtube.com/watch?v=wlnx-7cm4Gg) -- helped with creating StdOutListener class
* [Status Objects](https://gist.github.com/dev-techmoe/ef676cdd03ac47ac503e856282077bf2) -- easier to navigate than the documentation

# Future Ideas
* **Allow inputing account names instead of account IDs**
* Throw it onto a Raspberry Pi with a speaker, stream a junk Twitter in the config, and use it as a mini-Alexa in my dorm room
* Implement sentiment analysis
