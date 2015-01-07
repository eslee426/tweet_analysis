************************************************************************
date: November 20th, 2013
files: TweetSentiment.py and TweetSentimentMain.py
************************************************************************

TweetSentimentMain.py

def main():
This class asks user for the tweet file and outfile. It will then create an 
empty list to store the tweets in. It will call the tweet_reader function to
obtain each line of the file, which it will create a dictionary from the line. 
It will then add the dictionary to the list of tweets. It will then call the
add_geo function to find the state and zip code for each tweet dictionary in
the list. It will then ask for the sentiment value csv file, and then call
the sentiment_reader function to read the file. It will then call the 
add_sentiment function to add sentiment values for each tweet dictionary in the
list. It will then write each tweet with the new information into the 
outfile using the write_tweets method. To handle text file errors, if a 
dictionary from the make_tweet function returns a None, it will not insert
that dictionary into the list of tweets. 

It will then test the tweet_filter function, and write the filtered tweets in
an outfile. IT will also calculate the average sentiment value of the tweet 
value

It will then test the most_positive and most_negative functions and write
each tweets into their specific outfile. It will Print the state with the
most positive and most negative, as well as their average sentiment value.


Phase 1:

TweetSentiment.py

def make_tweet(tweet_line):
Given a string input of a line from a text file, it will strip the line of tabs
and put each element of the string in an array. It will then format and assign
each element. It will assign lat and long to its corresponding float values, 
create a datetime object for the time, and represent to tweet string in 
lowercase letters. It will then create and return a  dictionary:

    Dictionary keys:
    text  -- A string; the text of the tweet, all in lowercase
    time  -- A datetime object; the time that the tweet was posted
    lat   -- A number; the latitude of the tweet's location
    lon   -- A number; the longitude of the tweet's location

To handle text file errors, if the text file does not have all the needed
information, it will return None.



def tweet_text(tweet):
Given a dictionary of a tweet, it will return the text of the tweet as a string

def tweet_words(tweet):
Given a dictionary of a tweet, it will remove any punctuation from the tweet
and place each word into list and return the list

def tweet_time(tweet):
Given a dictionary of a tweet, it will return the datetime object of the tweet

def tweet_location(tweet):
Given a dictionary of a tweet, it will return a tuple representation of the
tweet's location

def make_zip(zipcode):
Given a list of the zipcode information, it will return the corresponding
information as a dictionary:
    Dictionary keys:
    zip    -- A string; the sip code
    state   -- A string; Two-letter postal code for state
    lat    -- A number; latitude of zip code location
    lon    -- A number; longitude of zip code location
    city   -- A string; name of city assoicated with zip code

def find_zip(tweet, zip_list):
Given a tweet dictionary, and a list of zipcode info dictionaries, it will
represent the tweet location as a tuple, create an empty zip_info array(to
store the zip_code dictionary corresponding to the minimum distance found), and
it will create an arbitrary min_distance value. It will go through each element
of the zip_list. It will represent the location of the zipcode as a tuple. It
will then calculate the distance between the tweet and the zipcode. If the
distance calculated is smaller than the min_distance value, it will save
the distance and assign the zip_info to the corresponding dictionary. This 
function finds the state and zipcode in which the tweet was sent from. It will
return the zip code dictionary corresponding to the tweet's location.

def geo_distance(loc1,loc2):
Given a tuple representation of longitude and latitude of 2 locations, it 
will return the the great circle distance using Haversine's formula. 
I had help with this formula's python code from the following website:
http://nifty.stanford.edu/2013/denero-muralidharan-trends/geo.py.html

def add_geo(tweets):
Given a list of tweet dictionaries, it will find and add the new corresponding
state and zip key to each tweet dictionary. It will also create a list of zip
code information represented as dictionaries. It will first ask for the zip 
csvfile. It will then create an empty list to store the zip code information
dictionary. It will use the zip_reader function (which  returns each line 
represented as a list) to read each line of the zip csv file. It will then call
the make_zip function, which creates a dictionary representation of the zip 
info, and it will finally add the dictionary to the list that stores the zip
code information. Then, it will go through each item in the list of tweet
dictionary, use the find_zip function (which uses the tweet dictionary and the 
zip code info dictionary) to find the corresponding state and zip
code for the tweet. It will then add the state and zipcode keys to the 
corresponding tweet dictionary. 

def write_tweets(tweets, outfile):
Given a dictionary of tweets and an outfile, it will represent the tweet 
information as a string and write it into the outfile in format:
[latitude, longitude]    datetime    state    zipcode    sentiment val    tweet

def zip_reader(zip_file):
Given a csv file, it will first create an empty array. It will then skip
the first line of the file (which contains information). It will then 
read the csv file, strip the line of quotation marks, and insert each 
information into a list. It will then return the list of information

def tweet_reader(tweet_file):
Given a tweet file, it will first create an empty array, it will then read
each line of the file and place each line in an array. It will then return
the list.


Phase 2:

def sentiment_reader(sent_file):
Given a file of sentiment values, it will first create a dictionary. It will 
then read each line of the file adding key value pairs (key: word (String) 
value: sentiment value (Float)). It will return this dictionary.

def sentiment_value(word, sentiments):
Given a word and a dictionary of sentiment values, it will first check if
the dictionary has the given word. If it does, it will return the sentiment
value of the word. If the word is not in the dictionary, it will return None.

def add_sentiment(sentiments, tweets):
Given a list of tweets and a dictionary of sentiment values, it will go through
each tweet and find the list of words in the tweet using the tweet_words 
function. For each of the words in the tweet, it will find it's corresponding
sentiment value and then find the average sentiment value of all the words.
If the sentiment value of a word is None, it is not considered in the average.
It will then add the average sentiment value to the list of tweets.

def tweet_filter(tweets, **kwargs):
Given a list of tweets, it will filter through the list of tweets for the given
key word arguments. It will then return a filtered list of tweets. It filters
througha  brute force method, going through the 7 possible filters:
1. Just word
2. Just State
3. Just zipcode
4. Word and State
5. Word and Zipcode
6. State and Zipcode
7. Word, State and Zipcode

def average_sentiment(filtered_tweets):
Given a ist of filtered tweets, it will return the average sentiment value of
all the tweets. If the tweet has a sentiment value of None, it will not be
considered in the average.

def filter_by_state(filtered_tweets):
Given a list of filtered_tweets, it will sort the tweets according to the state
It will create a dictionary. (Key: state value: list of tweets. It will go 
through each item in the tweets. If the dictionary does not have the state key,
it will create a new key with the state, create an empty list, insert the tweet
into the list, and set the list as the key's value. IF the dictioanary already
has the key value, it will append the tweet to the list of tweets. It will then
return the dictionary of tweets sorted by state.

def most_positive(tweets, word): 
Given a list of tweets, It will first filter the list of tweets by the word
using the tweet_filter function. It will then sort the filtered list by state
using the filter_by_state function. It will go through each element of the
sorted by state dictionary, and find the average sentiment value of all the 
tweets corresponding to the state. If the average sentiment value is bigger
than the original value, it will save the key for the corresponding state. 
It will go through each element to find the max sentiment value and return the
state corresponding to that value. 

def most_negative(tweets, word): 
Given a list of tweets, It will first filter the list of tweets by the word
using the tweet_filter function. It will then sort the filtered list by state
using the filter_by_state function. It will go through each element of the
sorted by state dictionary, and find the average sentiment value of all the 
tweets corresponding to the state. If the average sentiment value is smaller
than the original value, it will save the key for the corresponding state. 
It will go through each element to find the min sentiment value and return the
state corresponding to that value. 
