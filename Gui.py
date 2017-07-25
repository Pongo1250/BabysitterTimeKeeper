import Babysitter
from Tkinter import *

root = Tk()
root.title("BabysitterTimeKeeper")

#Dictionaries for Dropdown menu
sTList= ["5p","6p", "7p", "8p", "9p", "10p", "11p", "12p","1a", "2a", "3a" ]
eTList = ["6p", "7p", "8p", "9p", "10p", "11p", "12p","1a", "2a", "3a", "4a" ]
bTList = ["5p","6p", "7p", "8p", "9p", "10p", "11p", "12p","1a", "2a", "3a", "4a"]

################# Drop Down Menus#####################
#Set start time variable to 5p by default
stimevar = StringVar(root)
stimevar.set("5p")

#Start time menu 
stimeMenu = OptionMenu(root, stimevar, *sTList)
Label(root, text = "Start Time").grid(row = 1, column = 1)
stimeMenu.grid(row = 1, column = 2)

#set end time variable to 6p by default
etimevar = StringVar(root)
etimevar.set("6p")

#End time menu
etimeMenu = OptionMenu(root, etimevar, *eTList)
Label(root, text = "End Time").grid(row = 2, column = 1)
etimeMenu.grid(row =2, column = 2)

#set bed time variable to 5p by default
btimevar = StringVar(root)
btimevar.set("5p")

#Bed Time Menu
btimeMenu = OptionMenu(root, btimevar, *bTList)
Label(root, text = "Bed Time").grid(row = 3, column = 1)
btimeMenu.grid(row = 3, column = 2)



# change drop down menu



root.mainloop()