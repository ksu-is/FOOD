import requests
import json

client_id = "CuyK_Nviuv3km8gryYuiqg"
api_key = "tGjtDDhoM96gsB8uJc8qEiBXB-xcU-60aXJ8yZfT9aBArhjYB1wplGaZNYIKUUyk-g5bvqkY2gZzdIsWKwbdoGudeRMXXTUiA1JjLAIY-kRnjy6eRnWjUK6fPOP2YHYx"
headers = {'Authorization': 'Bearer %s' % api_key}

url='https://api.yelp.com/v3/businesses/search'

search_terms = {'categories':'mexican','location':'30144'}

# Making a get request to the API
req=requests.get(url, params=search_terms, headers=headers)

# proceed only if the status code is 200
# print('The status code is {}'.format(req.status_code))

parsed_input = json.loads(req.text)

results = parsed_input["businesses"]

for i in results:
    if i["name"] == "Tacos Del Chavo":
        #print (i)
        break
    else:
        pass

for i in results:
    print ("<a href=\"" + i["url"] + "\">" + i["name"] + "</a>")

#print (results)
