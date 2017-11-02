import tweepy
import json

access_token = "    "
access_token_secret = " "
consumer_key = " "
consumer_secret = " "

class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Parsing 
        decoded = json.loads(data)
        #open a file to store the status objects
        file = open('tweepy.csv', 'w')  
        #write to file
        json.dump(decoded,file,sort_keys = True,indent = 4)
        #show progress
        print("Writing tweets to file,CTRL+C to terminate the program")

        
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = tweepy.Stream(auth, l)
    stream.filter(track=["#trump"])
