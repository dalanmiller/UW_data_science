#Homework 6

##0
15 tweets per page of the API

##1


##2
The score I calculated for Microsoft was at 180.

Basically I took all the Twitter data from 10 pages with 25 results per page, limited to English.
I then went through each tweet, changed to ascii, and used the nltk module to tokenize the sentences into words (and I think punctuation.) I then went through each word in the sentence and if it existed in the AFINN dictionary I added that value to the tweets total 'score'. I then summed all the scores of the tweets.

Code visible in hw6.py in this same repository.

##3
Over 60 seconds I got 2040 tweets.
2040 / 60 = 34 tweets per second.
34 tweets per second * 100 == 3400 tweets per second during my 60 second sample.

##4

Ultimately, I completely overthought this problem. At first I didn't realize that the Twitter data could contain the city, state data.
So I spent an inordinate amount of time (at least 6 hours) trying to reverse geocode every tweet if possible which resulted in a lot of frustration from limitations of reverse geocoding APIs.
Finally I realized my mistake and was able to narrow down the
10,000,000+ tweets I had collected to the ones that contained geocode data, were in the United States, and had place_type of 'city' which was only about 40,000.
I then used the same AFINN analysis used for the Microsoft problem above, and came up with the following list.

<pre>{u'AL': -11,
 u'AR': -3,
 u'AZ': 0,
 u'CA': 29,
 u'CO': 3,
 u'CT': 14,
 u'DC': -6,
 u'DE': -2,
 u'FL': 0,
 u'GA': -24,
 u'HI': 11,
 u'IA': 4,
 u'IL': 9,
 u'IN': -1,
 u'KS': -3,
 u'KY': -4,
 u'LA': -5,
 u'MA': -14,
 u'MD': -11,
 u'ME': -3,
 u'MI': 50,
 u'MN': -1,
 u'MO': -11,
 u'MS': 1,
 u'NC': -11,
 u'ND': 0,
 u'NE': -3,
 u'NH': -9,
 u'NJ': 14,
 u'NM': -6,
 u'NV': -3,
 u'NY': 22,
 u'OH': 5,
 u'OK': 2,
 u'OR': 20,
 u'PA': 32,
 u'PR': 2,
 u'RI': 4,
 u'SC': 2,
 u'SD': -4,
 u'TN': 22,
 u'TX': -25,
 u'UT': -7,
 u'VA': -7,
 u'VT': 1,
 u'WA': 26,
 u'WI': 11,
 u'WV': 10,
 u'WY': 0}</pre>


##5

I'm quite confused as to why out of 10 million tweets taken over the course of several days that there were none given 'lang':'en',
That happened to be in the middle of the day. I don't think it had to do with my MongoDB aggregation query which can be seen in hw6.py. 
Basically I took a substr of the time value for the hour and then did the equivalent of a GROUP BY on that hour and created a giant list of
all the tweets that I was then able to more easily run through with Python, doing a AFINN analysis on each. 

![Bar Chart for Hours v Mood](https://github.com/dalanmiller/UW_data_science/raw/master/hw6.png)
