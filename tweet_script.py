import twitter
import json

credentials_file = open('credentials')
credentials_file_data = credentials_file.read()
credentials_data = json.loads(credentials_file_data)

print(credentials_data)

api = twitter.Api(consumer_key=credentials_data["key"],
		  consumer_secret=credentials_data["secret"],
		  access_token_key=credentials_data["access_token"],
		  access_token_secret=credentials_data["access_token_secret"])

print(api.VerifyCredentials())
