from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
#from base64 import b16encode, b16decode

access_token = ""
access_token_secret = ""

consumer_key = ""
consumer_secret = ""

"""
#{"user": {"follow_request_sent": null, "profile_use_background_image": true, "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/555044729/city-of-love_1_.png", "verified": false, "profile_image_url_https": "https://si0.twimg.com/profile_images/2911526228/33bda27f2866251ebbf62feb27742a28_normal.jpeg", "profile_sidebar_fill_color": "C9C9C9", "id": 445521847, "profile_text_color": "1C1F23", "followers_count": 291, "protected": false, "id_str": "445521847", "default_profile_image": false, "location": null, "utc_offset": -32400, "statuses_count": 19040, "description": "19,Nbhs; Seniors'13 Instagram: @sweetescape_x3", "friends_count": 319, "profile_link_color": "FFB570", "profile_image_url": "http://a0.twimg.com/profile_images/2911526228/33bda27f2866251ebbf62feb27742a28_normal.jpeg", "notifications": null, "geo_enabled": false, "profile_background_color": "FFFFFF", "profile_banner_url": "https://si0.twimg.com/profile_banners/445521847/1353276880", "profile_background_image_url": "http://a0.twimg.com/profile_background_images/555044729/city-of-love_1_.png", "screen_name": "SweetEscape_x3", "lang": "en", "following": null, "profile_background_tile": true, "favourites_count": 249, "name": "Kathy Pena", "url": null, "created_at": "Sat Dec 24 14:15:26 +0000 2011", "contributors_enabled": false, "time_zone": "Alaska", "profile_sidebar_border_color": "BFBFBF", "default_profile": false, "is_translator": false, "listed_count": 0}, "favorited": false, "entities": {"user_mentions": [{"indices": [3, 17], "id": 371504567, "screen_name": "DrizzyParrax7", "id_str": "371504567", "name": "David Parra"}], "hashtags": [], "urls": []}, "retweeted_status": {"user": {"follow_request_sent": null, "profile_use_background_image": true, "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme9/bg.gif", "verified": false, "profile_image_url_https": "https://si0.twimg.com/profile_images/2909442947/8331b682b9351ac6763b5c94190f457a_normal.jpeg", "profile_sidebar_fill_color": "252429", "id": 371504567, "profile_text_color": "666666", "followers_count": 464, "protected": false, "id_str": "371504567", "default_profile_image": false, "location": "Cliffside Park, New Jersey", "utc_offset": -28800, "statuses_count": 26433, "description": "Class of '13.", "friends_count": 779, "profile_link_color": "2FC2EF", "profile_image_url": "http://a0.twimg.com/profile_images/2909442947/8331b682b9351ac6763b5c94190f457a_normal.jpeg", "notifications": null, "geo_enabled": false, "profile_background_color": "1A1B1F", "profile_banner_url": "https://si0.twimg.com/profile_banners/371504567/1353421555", "profile_background_image_url": "http://a0.twimg.com/images/themes/theme9/bg.gif", "screen_name": "DrizzyParrax7", "lang": "en", "following": null, "profile_background_tile": false, "favourites_count": 2957, "name": "David Parra", "url": null, "created_at": "Sun Sep 11 00:20:28 +0000 2011", "contributors_enabled": false, "time_zone": "Pacific Time (US & Canada)", "profile_sidebar_border_color": "181A1E", "default_profile": false, "is_translator": false, "listed_count": 0}, "favorited": false, "entities": {"user_mentions": [], "hashtags": [], "urls": []}, "contributors": null, "truncated": false, "text": "THAT'S BIG SEAN'S PART YOU FUCK.", "created_at": "Wed Dec 05 03:29:46 +0000 2012", "retweeted": false, "in_reply_to_status_id_str": null, "coordinates": null, "in_reply_to_user_id_str": null, "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>", "in_reply_to_status_id": null, "place": null, "id_str": "276166445715570689", "in_reply_to_screen_name": null, "retweet_count": 0, "geo": null, "id": 276166445715570689, "in_reply_to_user_id": null}, "truncated": false, "text": "RT @DrizzyParrax7: THAT'S BIG SEAN'S PART YOU FUCK.", "created_at": "Wed Dec 05 03:30:37 +0000 2012", "retweeted": false, "in_reply_to_status_id_str": null, "coordinates": null, "in_reply_to_user_id_str": null, "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>", "in_reply_to_status_id": null, "place": null, "id_str": "276166661407645696", "contributors": null, "in_reply_to_screen_name": null, "retweet_count": 0, "geo": null, "id": 276166661407645696,
"""
class StdOutListener(StreamListener):
	""" A listener handles tweets are the received from the stream. 
	This is a basic listener that just prints received tweets to stdout.

	"""
	def __init__(self):
	    self.output = open('output.json','a')
	    self.bad_list = [
			'profile_background_image_url_https',
			'profile_image_url_https',
			'source',
			'entities',
			'profile_use_background_image',
			'following',
			'hashtags',
			'contributors',
			'profile_link_color',
			'verified',
			'profile_text_color',
			'protected',
			'profile_image_url',
			'profile_background_color',
			'retweeted_status',
			'retweet_count',
			'user'
			]

	def on_data(self, data):
        		tweet = json.loads(data)
		        if 'lang' not in tweet or tweet['lang'] == 'en':
				for x in self.bad_list:
					try:
						del tweet[x]
					except:							
						continue					
               			self.output.write(json.dumps(tweet))
	           	    	self.output.write('\n')
	               		return True
		
	def on_error(self, status):
		return True

if __name__ == '__main__':
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	stream = Stream(auth, l)	
	stream.sample()
