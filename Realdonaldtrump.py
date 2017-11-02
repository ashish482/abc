import tweepy
import csv

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


def get_all_tweets(screen_name):
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print("getting tweets before %s",(oldest))
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print("...%s tweets downloaded so far",(len(alltweets)))

	user=api.get_user(25073877)	
        outtweets = [[user.screen_name,user.name,user.followers_count,tweet.user.id,tweet.place,tweet.created_at,tweet.id_str,tweet.text.encode("utf-8"),tweet.source,tweet.retweeted,tweet.in_reply_to_screen_name,tweet.in_reply_to_user_id] for tweet in alltweets]
        f=open('Realdonaldtrump.csv', 'w')
        a = csv.writer(f)
        a.writerow(["name","username","Total followers","User ID","User place","Date of tweet","Tweet id","Tweet text","Tweet source","Tweet Retweeted","Tweet reply to name""id","Tweet reply to ID"])
        a.writerows(outtweets)
	f.close
	
	


if __name__ == '__main__':
	get_all_tweets("realDonaldTrump")
