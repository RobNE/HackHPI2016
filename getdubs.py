import requests
import os
import hashlib
import base64
import sys
import urllib

URL = 'https://dubhack.dubsmash.com'


CLIENT_ID = 'xxx'
CLIENT_SECRET = 'xxx'
USERNAME = 'xxx'
PASSWORD = 'xxx'

login_data = {
    'username': USERNAME,
    'password': PASSWORD,
    'grant_type': 'password',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
}

# Login to get access token
login_response = requests.post('{0}/me/login'.format(URL), json=login_data)
access_token = login_response.json()['access_token']

# Creating the Authorization header for following requests
headers = {
    'Authorization': 'Bearer {0}'.format(access_token),
    'content-type': 'application/json'
}

emotion = sys.argv[1]

trending_snips = requests.get(('{0}/snips/search?term='+emotion).format(URL), headers=headers)

snip = trending_snips.json()['results'][0]['data']

#print(trending_snips.json())

API_KEY = 'xxx'

file_name = snip['url'] #'https://d2nr8mwohhwyyc.cloudfront.net/snips/415769e7-fbe1-4d2e-9228-40b8bf6a7497.m4a'

#file_name = 'https://d2nr8mwohhwyyc.cloudfront.net/snips/2a62dd5d-5267-4463-8d5a-ede48e5dfd80.aac'

#file_name = 'https%3A%2F%2Fd2nr8mwohhwyyc.cloudfront.net%2Fsnips%2F1e2aaf7f-f270-4f04-bff8-78724105cdc9.aac'

#URL_encoded = urllib.urlencode({'apikey': API_KEY, 'inputformat': file_name[-3:], 'outputformat': 'ogg', 'input': 'download', 'file': file_name, 'wait': 'true', 'download': 'false'})
#URL_encoded_full = 'https://api.cloudconvert.com/convert?'+URL_encoded

#print('Converter: '+ URL_encoded_full)
file_name_url_encoded = urllib.urlencode({'file' : file_name}) #'file='+file_name

request_string = 'https://api.cloudconvert.com/convert?apikey='+API_KEY+'&inputformat='+file_name[-3:]+'&outputformat=ogg&input=download&'+file_name_url_encoded+'&wait=true&download=false'

print('Request string: '+request_string)

converted = requests.get(request_string)

print('Converted response' + str(converted.json()))

converted_URL = 'https:'+converted.json()['output']['url']

print('Converted URL: '+ converted_URL)

sentiments = requests.post('https://noderedprototypehackhpi.eu-gb.mybluemix.net/postAudioUrl', data=converted_URL)

snip_slug_sents = {'slug': snip['slug'], 'sentiments': sentiments.json()['document_tone']['tone_categories'][0]['tones']}

print('Slug & Sentiments'+ str(snip_slug_sents))




