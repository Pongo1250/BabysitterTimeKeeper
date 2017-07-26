import Babysitter
from Tkinter import *

root = Tk()
root.title("BabysitterTimeKeeper")


##########FUNCTIONS##############
#creates popup window that tells you how much to charge
def calculateBill():
    bill = Toplevel()
    bill.wm_title("Babysitter Bill")
    
    #Time Information
    l = Label(bill, text="Your bill for the customer:").grid(sticky = "w",row=0, column=0)
    space =Label(bill, text = "" ).grid(row = 2)
    if(Babysitter.timeCheck(stimevar.get(),etimevar.get()) == "true"):
    	time = Label(bill, text = "You babysat from " + stimevar.get() +" - "+ etimevar.get()).grid(sticky = "w",row = 3, column = 0)
    	
    	if(Babysitter.bedCheck(stimevar.get(), etimevar.get(), btimevar.get()) == "true"):
    		bedT = Label(bill, text = "Bedtime was " + btimevar.get()).grid(sticky = "w",row = 4, column = 0)
    		space1 = Label(bill, text = "" ).grid(row = 5)
    		l1 = Label(bill, text ="Pay Breakdown:").grid(sticky = "w",row = 6, column = 0)
    		#split times into integers for math and assign to variables
    		stime = Babysitter.timeSplit(stimevar.get())
    		etime = Babysitter.timeSplit(etimevar.get())
    		btime = Babysitter.timeSplit(btimevar.get())

    		#time breakdown 
    		SToBHours = btime - stime
    		if(btime< 12):
    			if (etime <12):
    				BToMHours = etime - btime
    			else:
    				BToMHours = 12 - btime
    		else:
    			BToMHours = 0
    		if(etime > 12):
    			MToEHours = etime -12
    		else:
    			MToEHours = 0
    		TotHours = SToBHours + BToMHours + MToEHours

    		#dollar values
    		SToBVal = Babysitter.SToBPay(stime, btime)
    		BToMVal = Babysitter.BToMPay(btime, etime)
    		MToEVal = Babysitter.MToEPay(etime)

    		Total = SToBVal + BToMVal + MToEVal

    		#Start time to Bed time pay label
    		SPay = Label(bill, text = "Start to Bedtime: " + str(SToBHours)+ " hours = ").grid(sticky = "w",row = 7, column = 0)
    		SToBPay = Label(bill, text = "$" + str(SToBVal)).grid(row = 7, column = 1)

    		#Bed Tiem to midnight pay label
    		MPay = Label(bill, text = "Bedtime to Midnight: " + str(BToMHours)+ " hours = ").grid(sticky = "w",row = 8, column = 0)
    		BToMPay = Label(bill, text = "$" + str(BToMVal)).grid(row = 8, column = 1)

    		#Midnight to Endtime pay Label
    		EPay = Label(bill, text = "Midnight to End: " + str(MToEHours) + " hours = ").grid(sticky = "w",row = 9, column = 0)
    		MToEPay = Label(bill, text = "$" + str(MToEVal)).grid(row = 9, column = 1)
    		
    		#Total
    		TPay = Label(bill, text = "Total Charge: " + str(TotHours) + " hours = ").grid(sticky = "w",row = 10, column = 0)
    		TotPay = Label(bill, text = "$" + str(Total)).grid(row = 10, column = 1)


    	else:
    		bedT = Label(bill, text = "Bedtime must be between start and end times").grid(sticky = "w",row = 4, column =0)
    else:
    	time = Label(bill, text = "start time must be before end time").grid(sticky = "w",row = 3, column = 0)


    #Pay Breakdown


    #Total




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

#Add Button to Calculate Charge
Label(root, text = "Calculate Pay").grid(row = 4, column = 1)
cpay = Button(root, text = "go", width = 6, command = calculateBill).grid(row = 4, column =2)




root.mainloop()