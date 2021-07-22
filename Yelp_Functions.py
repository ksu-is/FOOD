
import requests
import json


def parse_reply (parsed_input):

    businesses = parsed_input["businesses"]

    return (businesses)

def print_results (businesses_table):

    for business in businesses_table:
        print ("Name:", business["name"])
        print ("Rating:", business["rating"])
        print ("Address:", " ".join(business["location"]["display_address"]))
        print ("Phone", business["phone"])
        print ("Categories", business["categories"])
        print ("\n")

    return

def print_result (id, businesses_table):

    for business in businesses_table:
        if id == business["name"]:
            print ("Name:", business["name"])
            print ("Rating:", business["rating"])
            print ("Address:", " ".join(business["location"]["display_address"]))
            print ("Phone", business["phone"])
            print ("Categories", business["categories"])
            print ("\n")
            break
        else:
            pass

    return

def make_list (json_out):

    list_key = ["Name","Rating","Address","Phone","Categories","URL"]
    list_rest = []
    list_rest.append(list_key)
    #print (list_rest)
    for item in json_out:
        list_item = []
        list_item.append(item["name"])
        list_item.append(item["rating"])
        list_item.append(item["location"]["display_address"])
        list_item.append(item["phone"])
        list_item.append(item["categories"])
        id = get_buisness_id(item["name"],json_out)
        url = get_url(id, json_out)
        list_item.append(url)
      #  print (list_item)
    list_rest.append(list_item)

    return list_rest


def get_buisness_id (rname, business_table):

    for business in business_table:
        if rname == business["name"]:
            id = business["id"]
            break

    return (id)

def query_yelp (search_terms):

    client_id = "CuyK_Nviuv3km8gryYuiqg"
    api_key = "tGjtDDhoM96gsB8uJc8qEiBXB-xcU-60aXJ8yZfT9aBArhjYB1wplGaZNYIKUUyk-g5bvqkY2gZzdIsWKwbdoGudeRMXXTUiA1JjLAIY-kRnjy6eRnWjUK6fPOP2YHYx"
    headers = {'Authorization': 'Bearer %s' % api_key}

    url='https://api.yelp.com/v3/businesses/search'

    # Making a get request to the API
    req=requests.get(url, params=search_terms, headers=headers)
 
    # proceed only if the status code is 200
    # print('The status code is {}'.format(req.status_code))
 
    return json.loads(req.text)

def get_url (rest_id,business_table):
    
    for business in business_table:
        if rest_id == business["id"]:
            return (business["url"])
            

