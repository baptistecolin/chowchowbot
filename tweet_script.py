import twitter
import json
import sys, os

pic_path = sys.argv[1]


credentials_file = open('credentials')
credentials_file_data = credentials_file.read()
credentials_data = json.loads(credentials_file_data)

try:
	api = twitter.Api(consumer_key=credentials_data["key"],
		  consumer_secret=credentials_data["secret"],
		  access_token_key=credentials_data["access_token"],
		  access_token_secret=credentials_data["access_token_secret"])
except twitter.TwitterHTTPError as twittererror:
	print('authentication to Twitter failed :-\(')

print('posting picture ' + pic_path + '...')
try:
	status = api.PostUpdate(status='', media=pic_path)
except twitter.TwitterHTTPError as twittererror:
	print('Failure !!!')
