#! /usr/bin/env python

import os, sys, pprint

import requests, base64, json

from unidecode import unidecode


sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

from main.models import Tweet

CONSUMER_KEY = '9rCc3lx8eN6FmPoGWpDWYBUUM'
CONSUMER_SECRET = 'XkQgkmLTA5TJ6jbuGznBjCA4SZPio1zFo6VqcPVmUGN5JAuF51'

URL = 'https://api.twitter.com/oauth2/token'

SEARCH_TERM = 'techcrunch'

#base64 encode credentials

credentials = base64.urlsafe_b64encode('%s:%s' % (CONSUMER_KEY, CONSUMER_SECRET ))

#custom headers for the api keys

custom_headers = {
    'Authorization': 'Basic %s' % (credentials),
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',


}

grant_type_data = 'grant_type=client_credentials'

#putting it all together

response = requests.post(URL, headers=custom_headers, data=grant_type_data)

#what is this thing?
#print response.json()


#dump token to a variable

access_token = response.json().get('access_token')
# access_token = response.json()['access_token']  - Same as above
#print access_token

# custom for the search api
search_headers = {'Authorization': 'Bearer %s' % (access_token)}

#send the request
response = requests.get('https://api.twitter.com/1.1/search/tweets.json?q=%s&count=100' % SEARCH_TERM, headers=search_headers)


pp = pprint.PrettyPrinter(indent=2)

#print response.json().get('statuses')[0]['user'].keys()
# #print response.json().get('statuses')[0].keys()
# print "----"

# # print response.json().get('statuses')[0]['text']
# print response.json().get('statuses')[0]['user'].keys()
# print "--------"
# print response.json().get('statuses')[0]['user'].get('description')
# print "------------"
# print response.json().get('statuses')[0]['source']
# print "---------"

#print response.json().get('statuses')[0]['favorited']
#print "----------"
#print response.json().get('statuses')[0]['lang']

# pp.pprint(response.json().get('statuses')[0])

tweet_list = response.json().get('statuses')
print len(response.json().get('statuses'))

for tweet in tweet_list:

    print "@@  %s " % tweet.get('user').get('screen_name')
    tweet_obj, created = Tweet.objects.get_or_create(screen_name=tweet.get('screen_name'))
    
    tweet_obj.source = tweet.get('user').get('source')
    tweet_obj.location = tweet.get('user').get('location')
    tweet_obj.time_zone = tweet.get('user').get('time_zone')
    tweet_obj.created_at = tweet.get('user').get('created_at')
    tweet_obj.profile_image_url = tweet.get('user').get('profile_image_url')

    tweet_obj.save()
   

# for tweet in tweet_list:
#     tweet_location = tweet.get('user').get('location'),


#     if tweet_location != '' and tweet_location != None:

#         print "TWEET ---------"
#         print tweet.get('user').get('profile_image_url')
#         print tweet.get('user').get('screen_name')
#         print tweet.get('user').get('created_at')
#         print tweet.get('user').get('time_zone')
#         print tweet.get('user').get('location')
#         print "TWEET-TEXT----"
#         print tweet.get('text')

        
#include a field for search term on the Tweet model
    # #for data in response_dict['dataset']:
        
    #     tweets = Tweet.objects.get_or_create(name=(data.get('screen_name')))

    #     tweets = a_user.screen_name = str(data['screen_name'])
    #     tweets = a_user.location = str(data['location'])
    #     tweets.favourites_count = int(data['favourites_count']) 







# #{
#     u'token_type': u 'bearer',
#     u'acces_token: u'AAAAAAAAAAAAAAAAAAAAAAIRiQAAAAAARWrBgOl5ynVlgy0Vyf4GWXPO2KM%3D0UAJfBqDbOuxfTOFkyZCtQUHkpPCcLdHdseSKsydQBKRK5muNG'


# }
