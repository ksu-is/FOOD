import tkinter as tk
from tkinter import *
from tkinter import ttk


class karl(Frame):

    def __init__( self ):
        tk.Frame.__init__( self )
        genre = []
        self.american = False
        self.chinese = False
        self.mexican = False
        self.southern = False
        self.pack()
        self.master.title("F.O.O.D - F.O.O.D. Options Obtained Decisively")
        self.american = ttk.Checkbutton( self, text="American", width = 25, variable = self.american, onvalue=True, offvalue=False )
        self.chinese = ttk.Checkbutton( self, text="Chinese", width = 25, variable = self.chinese, onvalue=True, offvalue=False )
        self.mexican = ttk.Checkbutton( self, text="Mexican", width = 25, variable = self.mexican, onvalue=True, offvalue=False )
        self.southern = ttk.Checkbutton( self, text="Southern", width = 25, variable = self.southern, onvalue=True, offvalue=False )
        self.verify_choices = Button( self, text="Verify", width = 25, command = print(genre) )
        self.american.grid( row = 0, column = 1, columnspan = 1, sticky = W+E+N+S)
        self.chinese.grid( row = 0, column = 2, columnspan = 1, sticky = W+E+N+S)
        self.mexican.grid( row = 1, column = 1, columnspan = 1, sticky = W+E+N+S)
        self.southern.grid( row = 1, column = 2, columnspan = 1, sticky = W+E+N+S)
        self.verify_choices.grid( row = 2, column = 1, columnspan = 2, sticky = W+E+N+S)

    def new_window(self):
        self.newWindow = karl2()

    def close_window(self):
        self.destroy()

class karl2(Frame):
    
    def __init__(self):
        new = tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("Next Window")
        new.button = tk.Button( text = "Press to Close", width = 25, command = self.close_window)
        new.button.pack()
    
    def close_window(self):
        self.destroy()

def main():
    karl().mainloop()

if __name__ == '__main__':
    main()
