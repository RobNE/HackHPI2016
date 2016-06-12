import sys
import json
import ast
import operator
import requests
import urllib

chosenEmotion = sys.argv[1]
print(chosenEmotion)

if chosenEmotion == 'anger':
	with open('angry.json') as f:
		content = str(f.readlines())
elif (chosenEmotion == 'sadness'):
	with open('sad.json') as f:
		content = str(f.readlines())
elif (chosenEmotion == 'disgusted'):
	with open('disgusted.json') as f:
		content = str(f.readlines())
elif (chosenEmotion == 'fear'):
	with open('fear.json') as f:
		content = str(f.readlines())
elif (chosenEmotion == 'joy'):
	with open('joy.json') as f:
		content = str(f.readlines())

contentJson = ast.literal_eval(content)

#print(contentJson)

#print(content[0])
emotionValues = {}

for item in contentJson:
	emotion = item[13:16]
	if (emotion == "ang"):
		emotionIndex = item.find("u'Anger', u'score': ")
		slugIndex = item.find("'slug':")
		slug = item[slugIndex+10:slugIndex+16]
		emotionValues[slug] = item[emotionIndex+20:emotionIndex+28]
	elif (emotion == "sad"):
		emotionIndex = item.find("u'Sadness', u'score': ")
		slugIndex = item.find("'slug':")
		slug = item[slugIndex+10:slugIndex+16]
		emotionValues[slug] = item[emotionIndex+22:emotionIndex+30]
	elif (emotion == "dis"):
		emotionIndex = item.find("u'Disgust', u'score': ")
		slugIndex = item.find("'slug':")
		slug = item[slugIndex+10:slugIndex+16]
		emotionValues[slug] = item[emotionIndex+22:emotionIndex+30]
	elif (emotion == "fea"):
		emotionIndex = item.find("u'Fear', u'score': ")
		slugIndex = item.find("'slug':")
		slug = item[slugIndex+10:slugIndex+16]
		emotionValues[slug] = item[emotionIndex+19:emotionIndex+27]
	elif (emotion == "joy"):
		emotionIndex = item.find("u'Joy', u'score': ")
		slugIndex = item.find("'slug':")
		slug = item[slugIndex+10:slugIndex+16]
		emotionValues[slug] = item[emotionIndex+18:emotionIndex+26]

print(emotionValues)

maxValue = max(emotionValues.iteritems(), key=operator.itemgetter(1))[0]
print(maxValue)

URL = 'https://dubhack.dubsmash.com'
CLIENT_ID = 'Y3lFIamPITCru1IJHFGJ3jizI9lUTZhw9k0vxz84'
CLIENT_SECRET = 'i5M1vnBj9PUsJUSZjPqHadHVo2eednRrNlXeIr0e4I9vZXXuF69UHl2xZ12evYoo3m5kGsnE13utbIccXwXI1ybllL4hyAmeoMcQNXT2eXiaSLiZW070aUSpDViUIBsS'
USERNAME = 'sunny_berlin'
PASSWORD = 'hackhpi2016'

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

snip = requests.get(('{0}/snips/'+str(maxValue)).format(URL), headers=headers).json()

snip_url  = snip['url']

print(snip_url)

file = urllib.URLopener()
file.retrieve(snip_url)

#print(sorted(emotionValues))
#max_value = max(emotionValues)
#print(max_value)

