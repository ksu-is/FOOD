from tkinter import *
from tkinter import messagebox
from Yelp_Functions import *
import random


# A function to ensure a required field is not empty. This used to 
# prevent the zip code box from being left empty
# and ensure at least one genre is selected
def check_empty_choices() :

    #get the zip code entered and convert it to a string
    digits = str(zipCodeEntry.get())

    #Check to see if something was entered
    if digits == "":

        #if zip code is blank, display warning and return
        messagebox.showwarning(title="No Zip Code",message="A zipcode must be entered.")
        return
    else:
        #if a zip code was entered, check that it is exactly 5 characters long
        if len(digits) == 5:
            #if it is, try to convert to an integer
            try:
                int(digits)
            #If it will not convert, display warning and return    
            except:
                messagebox.showwarning(title="Invalid Zip Code", message="Zip Code must be all digits.")
                return
        #If the zip code was too long or too short, display an error and return
        else:
            messagebox.showwarning(title="Invalid Zip Code", message="Zip Code must be 5 numeric digits.")    
            return
        
    
    # Initialize the list to hold the acceptable genres
    genresList = []

    # This is the logic that assmbles the list of acceptable genres for the search.
    for i in masterGenreList:
        if i.get() != "0":
            genresList.append(i.get().capitalize())
   
    # Convert the genre list to a string
    global genres
    genres = ", ".join(genresList)
    
    #Check to see if at least one genre was checked
    if genres:
        myClick()
    #If not, display error and return
    else:
        messagebox.showwarning(title="No Genres",message="You must select at least one food genre.")
        return

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
            name = str(i["name"])
            #Ask if that is acceptable
            outMess = 'Is', name, 'okay?'
            outMessage = ' '.join(outMess)
            isThisOk = messagebox.askyesno("Choice Made!", outMessage)
            #if it is acceptable, tell them to enjoy and close the program
            if isThisOk:
                messagebox.showinfo("Enjoy", "Great! Ejoy!")
                root.destroy()
            #If not, make another attempt                
            else:
                #return
                rand_resturaunt(results)
        else:
            pass


# The logic for the reset button, clearing all the entries
def clearAll():
    zipCodeEntry.delete(0, END)
    americanBox.deselect()
    bagelsBox.deselect()
    barbequeBox.deselect()
    brazilianBox.deselect()
    breakfastBox.deselect()
    buffetsBox.deselect()
    burgersBox.deselect()
    cafeteriaBox.deselect()
    cajunBox.deselect()
    caribbeanBox.deselect()
    cheesesteaksBox.deselect()
    chineseBox.deselect()
    cubanBox.deselect()
    delisBox.deselect()
    dinersBox.deselect()
    fastfoodBox.deselect()
    gastropubsBox.deselect()
    indianBox.deselect()
    italianBox.deselect()
    japaneseBox.deselect()
    koreanBox.deselect()
    mediterraneanBox.deselect()
    mexicanBox.deselect()
    middleeasternBox.deselect()
    noodlesBox.deselect()
    pizzaBox.deselect()
    ramenBox.deselect()
    sandwichesBox.deselect()
    seafoodBox.deselect()
    southernBox.deselect()
    steakhousesBox.deselect()
    sushiBox.deselect()
    tacosBox.deselect()
    thaiBox.deselect()
    vegetarianBox.deselect()
    vietnameseBox.deselect()

# The logic for what happens when you clike the big red button.
def myClick():

    # Get the zip code from the input
    zipCode = zipCodeEntry.get()
    
    #Get the radius entry
    radiusValue = int(radius.get())

    # Assemble and display the confirmation message
    outputMessage = "Searching within " + str(radiusValue) + " miles of zip code " + str(zipCode) + " for the following genres: \n" + genres + "\n\nProceed?"
    resultAcceptable = messagebox.askyesno("Your Selections", outputMessage)

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

    # Confirm the pending search before proceeding
    if resultAcceptable:
        #setup the search terms
        #print (genres)
        rest_params = {'categories':genres,'location':zipCode, 'radius':radiusValue}
        #print (rest_params)
        #call the yelp function to query the yelp database
        parsed = query_yelp (rest_params)
        #print (parsed)
        #parse the results into a json formatted list
        global results 
        results = parse_reply (parsed)
        #print (results)
        if results:
            # call the function to randomly choose the resturaunt
            rand_resturaunt(results)
        else:
            #Display warning that no results were found.
            messagebox.showwarning(title="No Options Found", message="We found no options. Try either widening the radius or selecting more options")
     

    #If not confirmed, reset and start again
    else:
       clearAll()

    



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
zipCodeText.set("Enter your 5 digit zip code:")
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
american = StringVar()
bagels = StringVar()
barbeque = StringVar()
brazilian = StringVar()
breakfast = StringVar()
buffets = StringVar()
burgers = StringVar()
cafeteria = StringVar()
cajun = StringVar()
caribbean = StringVar()
cheesesteaks = StringVar()
chinese = StringVar()
cuban = StringVar()
delis = StringVar()
diners = StringVar()
fastfood = StringVar()
gastropubs = StringVar()
indian = StringVar()
italian = StringVar()
japanese = StringVar()
korean = StringVar()
mediterranean = StringVar()
mexican = StringVar()
middleeastern = StringVar()
noodles = StringVar()
pizza = StringVar()
ramen = StringVar()
sandwiches = StringVar()
seafood = StringVar()
southern = StringVar()
steakhouses = StringVar()
sushi = StringVar()
tacos = StringVar()
thai = StringVar()
vegetarian = StringVar()
vietnamese = StringVar()

# A master list of genres
masterGenreList = [american,bagels,barbeque,brazilian,breakfast,buffets,burgers,cafeteria,cajun,caribbean,cheesesteaks,chinese,cuban,delis,diners,fastfood,gastropubs,indian,italian,japanese,korean,mediterranean,mexican,middleeastern,noodles,pizza,ramen,sandwiches,seafood,southern,steakhouses,sushi,tacos,thai,vegetarian,vietnamese]

#Setup a frame containing the genre choices to make the gui look cleaner
foodGenreFrame = LabelFrame(root, text="Select Acceptable food genres:", pady=10, padx=10)

#setup the genre checkboxes
americanBox = Checkbutton(foodGenreFrame, text="American", variable = american, onvalue="american")
americanBox.deselect()
americanBox.grid(row=1, column=0)
bagelsBox = Checkbutton(foodGenreFrame, text="Bagels", variable = bagels, onvalue="bagels")
bagelsBox.deselect()
bagelsBox.grid(row=1, column=1)
barbequeBox = Checkbutton(foodGenreFrame, text="Barbeque", variable = barbeque, onvalue="barbeque")
barbequeBox.deselect()
barbequeBox.grid(row=1, column=2)
brazilianBox = Checkbutton(foodGenreFrame, text="Brazilian", variable = brazilian, onvalue="brazilian")
brazilianBox.deselect()
brazilianBox.grid(row=1, column=3)
breakfastBox = Checkbutton(foodGenreFrame, text="Breakfast", variable = breakfast, onvalue="breakfast")
breakfastBox.deselect()
breakfastBox.grid(row=1, column=4)
buffetsBox = Checkbutton(foodGenreFrame, text="Buffets", variable = buffets, onvalue="buffets")
buffetsBox.deselect()
buffetsBox.grid(row=1, column=5)
burgersBox = Checkbutton(foodGenreFrame, text="Burgers", variable = burgers, onvalue="burgers")
burgersBox.deselect()
burgersBox.grid(row=2, column=0)
cafeteriaBox = Checkbutton(foodGenreFrame, text="Cafeteria", variable = cafeteria, onvalue="cafeteria")
cafeteriaBox.deselect()
cafeteriaBox.grid(row=2, column=1)
cajunBox = Checkbutton(foodGenreFrame, text="Cajun", variable = cajun, onvalue="cajun")
cajunBox.deselect()
cajunBox.grid(row=2, column=2)
caribbeanBox = Checkbutton(foodGenreFrame, text="Caribbean", variable = caribbean, onvalue="caribbean")
caribbeanBox.deselect()
caribbeanBox.grid(row=2, column=3)
cheesesteaksBox = Checkbutton(foodGenreFrame, text="Cheesesteaks", variable = cheesesteaks, onvalue="cheesesteaks")
cheesesteaksBox.deselect()
cheesesteaksBox.grid(row=2, column=4)
chineseBox = Checkbutton(foodGenreFrame, text="Chinese", variable = chinese, onvalue="chinese")
chineseBox.deselect()
chineseBox.grid(row=2, column=5)
cubanBox = Checkbutton(foodGenreFrame, text="Cuban", variable = cuban, onvalue="cuban")
cubanBox.deselect()
cubanBox.grid(row=3, column=0)
delisBox = Checkbutton(foodGenreFrame, text="Delis", variable = delis, onvalue="delis")
delisBox.deselect()
delisBox.grid(row=3, column=1)
dinersBox = Checkbutton(foodGenreFrame, text="Diners", variable = diners, onvalue="diners")
dinersBox.deselect()
dinersBox.grid(row=3, column=2)
fastfoodBox = Checkbutton(foodGenreFrame, text="Fast Food", variable = fastfood, onvalue="fast food")
fastfoodBox.deselect()
fastfoodBox.grid(row=3, column=3)
gastropubsBox = Checkbutton(foodGenreFrame, text="Gastropubs", variable = gastropubs, onvalue="gastropubs")
gastropubsBox.deselect()
gastropubsBox.grid(row=3, column=4)
indianBox = Checkbutton(foodGenreFrame, text="Indian", variable = indian, onvalue="indian")
indianBox.deselect()
indianBox.grid(row=3, column=5)
italianBox = Checkbutton(foodGenreFrame, text="Italian", variable = italian, onvalue="italian")
italianBox.deselect()
italianBox.grid(row=4, column=0)
japaneseBox = Checkbutton(foodGenreFrame, text="Japanese", variable = japanese, onvalue="japanese")
japaneseBox.deselect()
japaneseBox.grid(row=4, column=1)
koreanBox = Checkbutton(foodGenreFrame, text="Korean", variable = korean, onvalue="korean")
koreanBox.deselect()
koreanBox.grid(row=4, column=2)
mediterraneanBox = Checkbutton(foodGenreFrame, text="Mediterranean", variable = mediterranean, onvalue="mediterranean")
mediterraneanBox.deselect()
mediterraneanBox.grid(row=4, column=3)
mexicanBox = Checkbutton(foodGenreFrame, text="Mexican", variable = mexican, onvalue="mexican")
mexicanBox.deselect()
mexicanBox.grid(row=4, column=4)
middleeasternBox = Checkbutton(foodGenreFrame, text="Middle Eastern", variable = middleeastern, onvalue="middle eastern")
middleeasternBox.deselect()
middleeasternBox.grid(row=4, column=5)
noodlesBox = Checkbutton(foodGenreFrame, text="Noodles", variable = noodles, onvalue="noodles")
noodlesBox.deselect()
noodlesBox.grid(row=5, column=0)
pizzaBox = Checkbutton(foodGenreFrame, text="Pizza", variable = pizza, onvalue="pizza")
pizzaBox.deselect()
pizzaBox.grid(row=5, column=1)
ramenBox = Checkbutton(foodGenreFrame, text="Ramen", variable = ramen, onvalue="ramen")
ramenBox.deselect()
ramenBox.grid(row=5, column=2)
sandwichesBox = Checkbutton(foodGenreFrame, text="Sandwiches", variable = sandwiches, onvalue="sandwiches")
sandwichesBox.deselect()
sandwichesBox.grid(row=5, column=3)
seafoodBox = Checkbutton(foodGenreFrame, text="Seafood", variable = seafood, onvalue="seafood")
seafoodBox.deselect()
seafoodBox.grid(row=5, column=4)
southernBox = Checkbutton(foodGenreFrame, text="Southern", variable = southern, onvalue="southern")
southernBox.deselect()
southernBox.grid(row=5, column=5)
steakhousesBox = Checkbutton(foodGenreFrame, text="Steakhouses", variable = steakhouses, onvalue="steakhouses")
steakhousesBox.deselect()
steakhousesBox.grid(row=6, column=0)
sushiBox = Checkbutton(foodGenreFrame, text="Sushi", variable = sushi, onvalue="sushi")
sushiBox.deselect()
sushiBox.grid(row=6, column=1)
tacosBox = Checkbutton(foodGenreFrame, text="Tacos", variable = tacos, onvalue="tacos")
tacosBox.deselect()
tacosBox.grid(row=6, column=2)
thaiBox = Checkbutton(foodGenreFrame, text="Thai", variable = thai, onvalue="thai")
thaiBox.deselect()
thaiBox.grid(row=6, column=3)
vegetarianBox = Checkbutton(foodGenreFrame, text="Vegetarian", variable = vegetarian, onvalue="vegetarian")
vegetarianBox.deselect()
vegetarianBox.grid(row=6, column=4)
vietnameseBox = Checkbutton(foodGenreFrame, text="Vietnamese", variable = vietnamese, onvalue="vietnamese")
vietnameseBox.deselect()
vietnameseBox.grid(row=6, column=5)


#Setup Action buttons
foodButtonFrame = LabelFrame(root, text="Show me where I'm eating!", padx=5, pady=5)
foodButton = Button(foodButtonFrame, text="FOOD!", command=check_empty_choices, bg="red", pady=20, padx=20)
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