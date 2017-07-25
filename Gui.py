import Babysitter
from Tkinter import *

root = Tk()
root.title("BabysitterTimeKeeper")

#Dictionaries for Dropdown menu
sTime = {"5p","6p", "7p", "8p", "9p"}
eTime = {}

#Set start time variable to 5p by default
stimevar = StringVar(root)
stimevar.set("5p")

popupMenu = OptionMenu(root, stimevar, *sTime)
Label(root, text = "Start Time").grid(row = 1, column = 1)
popupMenu.grid(row = 1, column = 2)

# change drop down menu



root.mainloop()