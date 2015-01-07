#************************************************************************
# Name: Eisha Lee
# date: November 20th, 2013
# file: TweetSentimentMain.py
#
# Executes TweetSentiment.py
#************************************************************************
import TweetSentiment2 as ts

def main():
    tweetFile = raw_input('Enter name of tweet file: ')
    outFile = raw_input('Enter name of out file: ')
    tweet_dict = []
    for item in ts.tweet_reader(tweetFile):
        single_dict = ts.make_tweet(item)
        if single_dict != None:
            tweet_dict.append(single_dict)
    ts.add_geo(tweet_dict)
    sentimentFile = raw_input('Enter name of sentiment file: ')
    sent_dict = ts.sentiment_reader(sentimentFile)
    ts.add_sentiment(sent_dict, tweet_dict)
    ts.write_tweets(tweet_dict, outFile)

    wordfilter = raw_input('Enter name of word filter out file: ')
    word = ts.tweet_filter(tweet_dict, word = 'yay')
    print 'average of word: ', ts.average_sentiment(word)
    ts.write_tweets(word, wordfilter)    
    statefilter = raw_input('Enter name of state filter out file: ')
    state = ts.tweet_filter(tweet_dict, state = 'TX')
    print 'average of state: ', ts.average_sentiment(state)
    ts.write_tweets(state, statefilter)    
    zipfilter = raw_input('Enter name of zip filter out file: ')
    zipcode = ts.tweet_filter(tweet_dict, zip = '61317')
    print 'average of zipcode: ', ts.average_sentiment(zipcode)
    ts.write_tweets(zipcode, zipfilter)
    wszfilter = raw_input('Enter name of word/state/zip filter out file: ')
    wordstatezip = ts.tweet_filter(tweet_dict, word = 'little', state = 'TX', \
    zip = '98275')
    print 'average of word/state/zip: ', ts.average_sentiment(wordstatezip)
    ts.write_tweets(wordstatezip, wszfilter)    

    neg = raw_input('Enter name of negaitve out file: ')
    negative = ts.tweet_filter(tweet_dict, word='sad')
    state_neg = ts.most_negative(tweet_dict, 'sad')
    print 'state with most negative: ', state_neg
    print 'average of most negative: ', ts.average_sentiment(negative)
    ts.write_tweets(negative, neg)
    pos = raw_input('Enter name of positive out file: ')
    positive = ts.tweet_filter(tweet_dict, word='happy')
    state_positive = ts.most_positive(tweet_dict, 'happy')
    print 'state with most positive: ', state_positive
    print 'average of most positive: ', ts.average_sentiment(positive)
    ts.write_tweets(positive, pos)


main()