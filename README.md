# TwitterTTS
A program that fetches tweets by using a list of keywords or screen names and then vocalizes them with text-to-speech.

## Usage
To run tweetreader.py, keys.py must be given authentication keys from a new Twitter app (if you don't know how, try [this](https://projects.raspberrypi.org/en/projects/getting-started-with-the-twitter-api). Next, download the following modules:
```
pip install tweepy
pip install pyttsx3
pip install pypiwin32
```
After this, set up with preferences in config.py and you should be good to go.

## Files
* tweetreader.py: runs the tweet streamer
* config.py: used to change streaming settings
* keys.py: location to put Twitter access keys

## Libraries
* Tweepy: streams tweets
* pyttsx3: used for tts

## References
* [LucidProgramming](https://www.youtube.com/watch?v=wlnx-7cm4Gg) -- helped with creating StdOutListener class
* [Status Objects](https://gist.github.com/dev-techmoe/ef676cdd03ac47ac503e856282077bf2) -- easier to navigate than the documentation

## Future Ideas
- [x] Allow inputing screen names instead of account IDs
- [ ] Allow using screen names and search terms in a single filter
- [x] Throw it onto a Raspberry Pi with a speaker, stream a junk Twitter in the config, and use it as a mini-Alexa in my dorm room
- [ ] Implement sentiment analysis
