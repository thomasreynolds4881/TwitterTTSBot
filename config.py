'''
mode 0: fetch from account list
mode 1: fetch with phrase list
mode 2: fetch by location
show_retweets: option to show or skip retweets
log_name: destination file in which to log tweets

'''

mode = 1
show_retweets = True
log_name = "tweetlog.txt"

phrase_list = ["test"]
account_list = ["Twitter"]
location_list = [-119.17,32.84,-71.71,44.33] #set to United States (bottom left coordinate and then upper right coordinate)
