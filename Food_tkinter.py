from tkinter import *
from tkinter import messagebox
from Yelp_Functions import *
import random

# This function picks a random resturant from the Yelp results
def rand_resturaunt(results_list):

    # Create a list of resturant ids, which is the unique idenifier yelp uses.
    rest_id = []
    for i in results_list:
        rest_id.append(i["id"])

    # Roll the dice for the random number
    lucky_strike = random.randint(1,len(rest_id))
    # Decrement the result to convert it from 1 to number to 0 to number
    lucky_strike -= 1
    
    # Step through the results
    for i in results_list:
        # Check to see if this entry's id matches the "winning" id.
        if i["id"] == rest_id[lucky_strike]:
            #This pops up the result window
            outMessage = "Congratulations! You're going to", str(i["name"]), "\n", str(i["url"])
            isThisOk = messagebox.askyesno("Choice Made!", outMessage)
            print(isThisOk)
        else:
            pass


# The logic for the reset button, clearing all the entries
def clearAll():
    zipCodeEntry.delete(0, END)
    americanBox.deselect()
    chineseBox.deselect()
    mexicanBox.deselect()
    southernBox.deselect()

# The logic for what happens when you clike the big red button.
def myClick():

    # Initialize the list to hold the acceptable genres
    genresList = []

    # A master list of genres
    masterList = [american, chinese, mexican, southern]

    # This is the logic that assmbles the list of acceptable genres for the search.
    for i in masterList:
        if i.get() != "0":
            genresList.append(i.get().capitalize())
   
    # Convert the genre list to a string
    genres = ", ".join(genresList)

    # Assemble and display the confirmation message
    outputMessage = "Zip Code: " + str(zipCodeEntry.get() + "\nGenres selected: \n" + genres + "\n\nProceed?")
    resultAcceptable = messagebox.askyesno("Your Selections", outputMessage)
    
    # Get the zip code from the input
    zipCode = zipCodeEntry.get()
    #zipCodeEntry.delete(0, END)

    #Get the radius entry
    radiusValue = int(radius.get())
    
    #convert the radius to meters, since that is what yelp uses
    if radiusValue == 1:
        radiusValue = 1610
    elif radiusValue == 5:
        radiusValue = 8047
    elif radiusValue == 10:
        radiusValue = 16094
    else:
        #else set it to Yelp's maxumum search radius
        radiusValue = 40000

    print (radiusValue)


    # Confirm the pending search before proceeding
    if resultAcceptable:
        #setup the search terms
        rest_params = {'term': genres,'location':zipCode, 'radius':radiusValue}
        #call the yelp function to query the yelp database
        parsed = query_yelp (rest_params)
        #parse the results into a json formatted list
        results = parse_reply (parsed)
        # call the function to randomly choose the resturaunt
        rand_resturaunt(results)

    #If not confirmed, reset and start again
    else:
        zipCodeEntry.delete(0, END)
        americanBox.deselect()
        chineseBox.deselect()
        mexicanBox.deselect()
        southernBox.deselect()
    #print (results)



# Create the gui object, set the name and icon
root = Tk()
root.title("FOOD - Food Options Obtained Decisively")
root.iconbitmap("food.ico")
#root.geometry("400x400")

#Setup zip Code entry frame
zipCodeFrame = LabelFrame(root, padx=5, pady=5)

#Setup the label for the zip code entry box
zipCodeText = StringVar()
zipCodelabel = Label(zipCodeFrame, textvariable=zipCodeText)
zipCodeText.set("Enter your zip code:")
zipCodelabel.grid(row=0, column=0)

# Setup the zip code input and put it in the zip code frame
zipCodeEntry = Entry(zipCodeFrame)
zipCodeEntry.grid(row=1,column=0)

#Setup the label for the radius entry box
radiusText = StringVar()
radiuslabel = Label(zipCodeFrame, textvariable=radiusText)
radiusText.set("Search Radius (miles):")
radiuslabel.grid(row=0, column=1)

# The radius entry box setup
radius = StringVar(zipCodeFrame)
options = ["1", "5", "10", "25"]
radiusEntry = OptionMenu (zipCodeFrame, radius, *options)
radius.set("5")
radiusEntry.grid(row=1, column=1)

#setup Checkboxes
american = StringVar()
chinese = StringVar()
mexican = StringVar()
southern = StringVar()

#Setup a frame containing the genre choices to make the gui look cleaner
foodGenreFrame = LabelFrame(root, text="Select Acceptable food genres:", pady=10, padx=10)

#setup the genre checkboxes
americanBox = Checkbutton(foodGenreFrame, text="American", variable = american, onvalue="american")
americanBox.deselect()
americanBox.grid(row=1, column=0)
chineseBox = Checkbutton(foodGenreFrame, text="Chinese", variable = chinese, onvalue="chinese")
chineseBox.deselect()
chineseBox.grid(row=1, column=1)
mexicanBox = Checkbutton(foodGenreFrame, text="Mexican", variable = mexican, onvalue="mexican")
mexicanBox.deselect()
mexicanBox.grid(row=2, column=0)
southernBox = Checkbutton(foodGenreFrame, text="Southern", variable = southern, onvalue="southern")
southernBox.deselect()
southernBox.grid(row=2, column=1)

#Setup Action buttons
foodButtonFrame = LabelFrame(root, text="Show me where I'm eating!", padx=5, pady=5)
#foodButtonFrame.pack(padx=10,pady=10)
foodButton = Button(foodButtonFrame, text="FOOD!", command=myClick, bg="red", pady=20, padx=20)
foodButton.pack()

# setup a button to clear/reset the entry form
clearButton = Button(root, text="Reset", command=clearAll)


#Set up GUI grid
zipCodeFrame.grid(row=1,column=3)
foodGenreFrame.grid(row=2,column=3, padx=5, pady=5)
clearButton.grid(row=5, column=3)
foodButtonFrame.grid(row=0, rowspan=5, column=4, columnspan=2)

#main loop
root.mainloop()