
import requests
import json

#This parses the data dump from yelp into a JSON file.
def parse_reply (parsed_input):

    businesses = parsed_input["businesses"]

    return (businesses)

# This prints all of the results in a human readable format. It is not used in the gui version
# but is left in place for debugging and other possible uses.
def print_results (businesses_table):

    # Step through the JSON, printing every entry
    for business in businesses_table:
        print ("Name:", business["name"])
        print ("Rating:", business["rating"])
        print ("Address:", " ".join(business["location"]["display_address"]))
        print ("Phone", business["phone"])
        print ("Categories", business["categories"])
        print ("\n")

    return

# This prints a single which matches the provided id. Again, not used in the gui
# version but left in place if needed for debugging or other future versions of 
# the application.
def print_result (id, businesses_table):

    # Step through the JSON, locate the entry for the provided ID and print it.
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

# This is an function for making a list out of the entries JSON file. I wrote it thinking
# it would be easier to manipulate a list. Then gaining familiarity with the JSON format,
# I realized this is just excess overhead.
def make_list (json_out):

    # Setup a header line list
    list_key = ["Name","Rating","Address","Phone","Categories","URL"]
    
    # Setup a list to end up being the list of lists
    list_rest = []
    
    # Add the header line to the list
    list_rest.append(list_key)
    
    # loop through adding each JSON entry to the list of lists
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

# A function to get the id for a given business name. Not used currently
def get_buisness_id (rname, business_table):

    # Loop through the search results
    for business in business_table:
        # if the entry matches the saught after name, set the id
        if rname == business["name"]:
            id = business["id"]
            break

    return (id)

# Main function for querying yelp
def query_yelp (search_terms):

    # These are yelp provided values for identifying which "app" is performing the search
    client_id = "CuyK_Nviuv3km8gryYuiqg"
    api_key = "tGjtDDhoM96gsB8uJc8qEiBXB-xcU-60aXJ8yZfT9aBArhjYB1wplGaZNYIKUUyk-g5bvqkY2gZzdIsWKwbdoGudeRMXXTUiA1JjLAIY-kRnjy6eRnWjUK6fPOP2YHYx"
    headers = {'Authorization': 'Bearer %s' % api_key}

    # Assigning the search url to a variable for ease of user.
    url='https://api.yelp.com/v3/businesses/search'

    # Making a get request to the API
    req=requests.get(url, params=search_terms, headers=headers)
 
    # Return the results of the query
    return json.loads(req.text)

# A function to return the URL to the Yelp page for the given resturaunt id
def get_url (rest_id,business_table):
    
    #loop through the restults
    for business in business_table:
        # test if the ids match
        if rest_id == business["id"]:
            # return the url
            return (business["url"])
            

