from os import listdir
import sys
import requests

emotions = ['sad', 'angry', 'joy', 'fear', 'disgusted']


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

for emotion in emotions:
	files = listdir(emotion)

	f = open(emotion+'.json', 'w')

	for file in files:
		snip_url = 'https://s3.eu-central-1.amazonaws.com/dubmotion/'+emotion+'/'+file
		sentiments = requests.post('https://noderedprototypehackhpi.eu-gb.mybluemix.net/postAudioUrl', data=snip_url)

		slug = file[:-4]

		snip = requests.get(('{0}/snips/'+slug).format(URL), headers=headers)

		snip_slug_sents = {'slug': slug, 'emotion': emotion, 'sentiments': sentiments.json()['document_tone']['tone_categories'][0]['tones'], 'snip': snip.json()}

		#output += snip_slug_sents
		f.write("%s\n" % snip_slug_sents)

		print(str(snip_slug_sents))

	f.close()