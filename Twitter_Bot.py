import elasticsearch
import tweepy

consumer_key = "changeme"
consumer_secret = "changem"
access_token_key = "change_me"
access_token_secret = "change_me"
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# authentication of access token and secret
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)


es = elasticsearch.Elasticsearch(http_auth =('elastic','changeme'))  # use default of localhost, port 9200

stuff = api.user_timeline(screen_name = 'realdonaldtrump', count =200, tweet_mode="extended", wait_on_rate_limit=True)

i = 0
for status in stuff:
    i = i+1
    es.index(index='donald', doc_type='tweet', id=i, body={
        'Author': status.author.name, 'Tweet_data': status.full_text
    })

    print (i)


