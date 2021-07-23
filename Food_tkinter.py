from tkinter import *
from tkinter import messagebox
from Yelp_Functions import *
import random


def rand_resturaunt(results_list):
    rest_id = []
    for i in results_list:
        rest_id.append(i["id"])

    #print ("Rest_id:", rest_id)
    #print ("Length:", len(rest_id))
    lucky_strike = random.randint(1,len(rest_id))
    lucky_strike -= 1
    #print ("LS:", lucky_strike)
    for i in results_list:
        if i["id"] == rest_id[lucky_strike]:
            outMessage = "Congratulations! You're going to", str(i["name"]), "\n", str(i["url"])
            isThisOk = messagebox.askyesno("Choice Made!", outMessage)
            print(isThisOk)
        else:
            pass


def clearAll():
    zipCodeEntry.delete(0, END)
    americanBox.deselect()
    chineseBox.deselect()
    mexicanBox.deselect()
    southernBox.deselect()

def myClick():

    genresList = []

    masterList = [american, chinese, mexican, southern]

    for i in masterList:
        if i.get() != "0":
            genresList.append(i.get().capitalize())
   
    genres = ", ".join(genresList)

    outputMessage = "Zip Code: " + str(zipCodeEntry.get() + "\nGenres selected: \n" + genres + "\n\nProceed?")
    resultAcceptable = messagebox.askyesno("Your Selections", outputMessage)
    #print (resultAcceptable)
    #myLabel1 = Label(root, text = zipCodeEntry.get())
    #myLabel1.grid(row=6, column=3)
    zipCode = zipCodeEntry.get()
    #zipCodeEntry.delete(0, END)

    if resultAcceptable:
        rest_params = {'term': genres,'location':zipCode}
        parsed = query_yelp (rest_params)
        results = parse_reply (parsed)
        rand_resturaunt(results)

    else:
        zipCodeEntry.delete(0, END)
        americanBox.deselect()
        chineseBox.deselect()
        mexicanBox.deselect()
        southernBox.deselect()
    #print (results)




root = Tk()
root.title("FOOD - Food Options Obtained Decisively")
root.iconbitmap("food.ico")
#root.geometry("400x400")

#Setup zip Code entry
zipCodeFrame = LabelFrame(root, text="Enter your zip code", padx=5, pady=5)
#zipCodeFrame.pack(padx=10,pady=10)
zipCodeEntry = Entry(zipCodeFrame)
zipCodeEntry.grid(row=0,column=0)

#setup Checkboxes
american = StringVar()
chinese = StringVar()
mexican = StringVar()
southern = StringVar()

foodGenreFrame = LabelFrame(root, text="Select Acceptable food genres:", pady=10, padx=10)

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


clearButton = Button(root, text="Reset", command=clearAll)


#Set up GUI grid
zipCodeFrame.grid(row=1,column=3)
foodGenreFrame.grid(row=2,column=3, padx=5, pady=5)
clearButton.grid(row=5, column=3)
foodButtonFrame.grid(row=0, rowspan=5, column=4, columnspan=2)


root.mainloop()