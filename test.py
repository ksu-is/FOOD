import requests
import json
import random

client_id = "CuyK_Nviuv3km8gryYuiqg"
api_key = "tGjtDDhoM96gsB8uJc8qEiBXB-xcU-60aXJ8yZfT9aBArhjYB1wplGaZNYIKUUyk-g5bvqkY2gZzdIsWKwbdoGudeRMXXTUiA1JjLAIY-kRnjy6eRnWjUK6fPOP2YHYx"
headers = {'Authorization': 'Bearer %s' % api_key}

url='https://api.yelp.com/v3/businesses/search'

search_terms = {'categories':'mexican','location':'30102', 'radius':'8047'}
#search_terms = {'categories':'mexican','location':'30144'}

# Making a get request to the API
req=requests.get(url, params=search_terms, headers=headers)

# proceed only if the status code is 200
# print('The status code is {}'.format(req.status_code))

parsed_input = json.loads(req.text)

results = parsed_input["businesses"]
item_count = 0
#for i in results:
#    if i["name"] == "Tacos Del Chavo":
#        
#        #print (i)
#        break
#    else:
#        pass

rest_id = []
for i in results:
    item_count += 1
#    print ("<a href=\"" + i["url"] + "\">" + i["name"] + "</a>")
    rest_id.append(i["id"])
    
print (i["categories"])

print (results)
print ("Count:", item_count)
#print ("Rest_id:", rest_id)
#print ("Length:", len(rest_id))
#lucky_strike = random.randint(0,19)
#print ("LS:", lucky_strike)
#for i in results:
#    if i["id"] == rest_id[lucky_strike]:
#        print ("Congratulations! You're going to", i["name"])
#         print ("<a href=\"" + i["url"] + "\">" + i["name"] + "</a>")
#    else:
#        pass

