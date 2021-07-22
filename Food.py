
import requests
import json
from Yelp_Functions import *

def get_zip():

    zip_code = input ("Enter a zip code for your search: ")

    return zip_code

def get_categories():

    x=" "
    categories = []

    print ("If you enter no restuarunt categories, all will be searched")
    while True:
        x = input ("Enter a type of food/restruaunt you are willing to accept (Enter to quit): ")
        if x == "":
            break
        else:
            y = "'" + x + "'"
            categories.append(y)

    if categories:
        categories_str = ' '.join(categories)
    else:
        categories_str = "*"

    return categories_str

def get_nocat():
    x=" "
    no_categories = []

    while True:
        x = input ("Enter a type of food/restruaunt you are not willing to accept (Enter to quit): ")
        if x == "":
            break
        else:
            no_categories.append(x)

    return no_categories

rest_params = {'term':'seafood','location':'30144'}

#rest_params = {'location': get_zip(), 'categories': get_categories()}
#print (get_nocat())
#print (rest_params)
parsed = query_yelp (rest_params)

results = parse_reply (parsed)


#print (results)
#print_results(results)

#test_id = get_buisness_id("Catfish House", results)

#print ("Catfish House", test_id)
#get_url(test_id,results)

#print(json.dumps(parsed, indent=4))

