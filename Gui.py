import Babysitter
from Tkinter import *

root = Tk()
root.title("BabysitterTimeKeeper")

#Dictionaries for Dropdown menu
sTime = {"5p","6p", "7p", "8p", "9p"}
eTime = {"6p", "7p", "8p"}

#Set start time variable to 5p by default
stimevar = StringVar(root)
stimevar.set("5p")

#Start time menu 
stimeMenu = OptionMenu(root, stimevar, *sTime)
Label(root, text = "Start Time").grid(row = 1, column = 1)
stimeMenu.grid(row = 1, column = 2)

#set end time variable to 6p by default
etimevar = StringVar(root)
etimevar.set("6p")

#End time menu
etimeMenu = OptionMenu(root, etimevar, *eTime)
Label(root, text = "End Time").grid(row = 2, column = 1)
etimeMenu.grid(row =2, column = 2)

# change drop down menu



root.mainloop()