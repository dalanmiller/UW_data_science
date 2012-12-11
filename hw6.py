from collections import defaultdict
import datetime
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import nltk
import numpy as np
import os
import pprint
import pymongo
import re
import requests
import shelve
import simplejson as json
import string

shelf = shelve.open('hw6_shelf')

def init_twitter_analysis(query='microsoft', pages=10, rpp=25):
    """
    Load the shelve with some tweets
    """

    afinn = {}
    #Create AFINN dict
    with open('assignment6/AFINN-111.txt') as a6:
        for line in a6:
            split = [x.strip() for x in line.split('\t')]
            afinn[split[0]] = split[1]


    tweets = []
    #Get results
    # for x in xrange(1,10):
    #     url = 'https://search.twitter.com/search.json?lang=en'
    #     url += 'q=%s' % (query)
    #     url += '&rpp=%s' % (rpp)
    #     url += '&page=%s' % (pages)
    #     r = requests.get(url)
    #     results = json.loads(r.content)['results']
    #     tweets = tweets + results

    # print 'tweets =', len(tweets)

    shelf['afinn'] = afinn

def microsoft_analysis():
    shelf = shelve.open('hw6_shelf')
    tweets = shelf['tweets']

    #print 'Start Length', len(tweets)



    #Got 180 for microsoft
    return afinn_analysis(tweets)

def single_afinn_analysis(tweet):
    afinn = shelf['afinn']

    #Set initial values
    score = 0

    #Fix pesky text
    tweet = tweet.encode('ascii','replace')

    #Split of lowercase words using nltk tokenize to auto split
    split = [x.lower() for x in nltk.tokenize.word_tokenize(tweet)]

    #For each word in the tweet text split
    for word in split:

        #Check if the word exists in the AFINN dictionary
        if word in afinn:


            #Add AFINN word value to the tweets 'score'
            score += int(afinn[word])

    return score


def afinn_analysis(tweets):
    shelf = shelve.open('hw6_shelf')
    afinn = shelf['afinn']

    for t in tweets:

        #Although I did eventually make sure the API request only returns
        # 'en' results, this did help for skipping the non-english tweets
        # and removing them from the end result
        # if t['iso_language_code'] != 'en':
        #     tweets.remove(t)
        #     continue

        #Set initial values
        t['score'] = 0
        t['calculation_done'] = False

        #Fix pesky text
        t['text'] = t['text'].encode('ascii','replace')

        #Split of lowercase words using nltk tokenize to auto split
        split = [x.lower() for x in nltk.tokenize.word_tokenize(t['text'])]

        #For each word in the tweet text split
        for word in split:

            #Check if the word exists in the AFINN dictionary
            if word in afinn:

                #Wanted to separate the tweets which had no words which
                # were also in the AFINN dict and tweets which had words but
                # ultimately did equal a 'neutral' 0
                if t['calculation_done'] != True:
                    t['calculation_done'] = True

                #Add AFINN word value to the tweets 'score'
                t['score'] += int(afinn[word])


    #Print list of tweet scores which actually had words that existed in AFINN
    final_tweets = [t['score'] for t in tweets if t['calculation_done'] == True]
    print final_tweets

    shelf.close()
    return sum( final_tweets )

def open_json_return_tweets(path):
    #assert(os.path.isdir(path))
    with open(path) as json_file:
        tweets = []

        for line in json_file:
            line = line.encode("ascii",'replace')
            tweets.append(line)

    return tweets



if __name__ == '__main__':

    #init_twitter_analysis( )

    #microsoft_analysis()

    # tweets = open_json_return_tweets('./assignment6/monday_afternoon.json')
    #tweets = tweets + open_json_return_tweets('./assignment6/tuesday_morning.json')
    # shelf = shelve.open('hw6_shelf')
    # shelf['tweets'] = tweets
    # shelf.close()
    # print len(tweets)

    # path = '/Users/w6ue/Downloads/output'
    conn = pymongo.Connection('localhost')
    db = conn['twitter']

    # for letter in string.lowercase[:10]: # a-j

    #     tweets = open_json_return_tweets(path+letter)

    #     print len(tweets)

    #     for t in tweets:
    #         try:
    #             temp = json.loads(t)
    #             if 'id' in temp:
    #                 db.tweets.update({'id':temp['id']}, temp, upsert=True)
    #             else:
    #                 db.tweets.insert(temp)
    #         except:
    #             print 'FAIL'
    #             continue

    # results = db.tweets.find(
    #     {'geo':{'$ne': None },'lang':'en', 'place.country_code':'US', 'place.place_type':'city' },
    #     {'text':True, 'place.full_name':True, '_id':False})

    # final_results = defaultdict(dict)

    # for r in results:
    #     state = r['place']['full_name'].split(',')[1].lstrip()
    #     if state not in final_results:
    #         final_results[state] = 0
    #     final_results[state] += single_afinn_analysis(r)


    # pprint.pprint(dict(final_results))

    # results = db.tweets.find({
    #         'text':{'$exists':True},
    #         'created_at':{'$exists':True}
    #     },{
    #         '_id':False, 'text':True,'created_at':True
    #     }).limit(1000000)

    result = db.tweets.aggregate(
        [
        {'$match': {'lang':'en', 'text':{'$exists':True}, 'created_at':{'$exists':True}}},
        {'$project':{ 'created_at': {'$substr':[ "$created_at", 11,2 ]}, '_id':False, 'text':True }},
        {'$group':{'_id':'$created_at', 'text': {'$addToSet':'$text'}}}
        ])

    r_dict = {x["_id"]:0 for x in result['result']}
    print r_dict

    for r in result['result']:
        for t in r['text']:
            r_dict[r['_id']] += single_afinn_analysis(t)

    pprint.pprint(r_dict)

    plt.bar(map(int,r_dict.keys()), r_dict.values())
    plt.xlabel('Hour of Day')
    plt.ylabel('Mood')
    plt.title(r'Histogram of Tweets mapped Hour of Day to Mood')
    plt.grid(True)

    plt.show()













