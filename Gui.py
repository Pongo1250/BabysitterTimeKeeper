import Babysitter
from Tkinter import *

#creates main program window
root = Tk()
root.title("BabysitterTimeKeeper")


##########FUNCTIONS##############
#creates popup window that tells you how much to charge and gives you a breakdown
#of cost and hours.
def calculateBill():
	#creates new window
    bill = Toplevel()
    bill.wm_title("Babysitter Bill")
    
    #Time Information
    l = Label(bill, text="Your bill for the customer:").grid(sticky = "w",row=0, column=0)
    space =Label(bill, text = "" ).grid(row = 2)
    #checks to see that times are valid
    if(Babysitter.timeCheck(stimevar.get(),etimevar.get()) == "true"):
    	time = Label(bill, text = "You babysat from " + stimevar.get() +" - "+ etimevar.get()).grid(sticky = "w",row = 3, column = 0)
    	#checks to see if bed time is valid
    	if(Babysitter.bedCheck(stimevar.get(), etimevar.get(), btimevar.get()) == "true"):
    		bedT = Label(bill, text = "Bedtime was " + btimevar.get()).grid(sticky = "w",row = 4, column = 0)
    		space1 = Label(bill, text = "" ).grid(row = 5)
    		l1 = Label(bill, text ="Pay Breakdown:").grid(sticky = "w",row = 6, column = 0)
    		lr = Label(bill, text ="Pay Rate").grid(sticky = "w",row = 6, column = 1)
    		lp = Label(bill, text ="Pay").grid(sticky = "w",row = 6, column = 2)
    		#split times into integers for math and assign to variables
    		stime = Babysitter.timeSplit(stimevar.get())
    		etime = Babysitter.timeSplit(etimevar.get())
    		btime = Babysitter.timeSplit(btimevar.get())

    		#time breakdown 
    		SToBHours = btime - stime
    		#checks that bedtime is before 12
    		if(btime< 12):
    			#modifies BToMHours if etime is before 12
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
    		SRate = Label(bill, text ="$12/hr").grid(sticky = "w",row = 7, column = 1)
    		SToBPay = Label(bill, text = "$" + str(SToBVal)).grid(row = 7, column = 2)

    		#Bed Time to midnight pay label
    		MPay = Label(bill, text = "Bedtime to Midnight: " + str(BToMHours)+ " hours = ").grid(sticky = "w",row = 8, column = 0)
    		MRate = Label(bill, text ="$8/hr").grid(sticky = "w",row = 8, column = 1)
    		BToMPay = Label(bill, text = "$" + str(BToMVal)).grid(row = 8, column = 2)

    		#Midnight to Endtime pay Label
    		EPay = Label(bill, text = "Midnight to End: " + str(MToEHours) + " hours = ").grid(sticky = "w",row = 9, column = 0)
    		ERate = Label(bill, text ="$16/hr").grid(sticky = "w",row = 9, column = 1)
    		MToEPay = Label(bill, text = "$" + str(MToEVal)).grid(row = 9, column = 2)
    		
    		#Total
    		TPay = Label(bill, text = "Total Charge: " ).grid(sticky = "w",row = 10, column = 0)
    		TotPay = Label(bill, text = "$" + str(Total)).grid(row = 10, column = 2)


    	else:
    		bedT = Label(bill, text = "Bedtime must be between start and end times").grid(sticky = "w",row = 4, column =0)
    else:
    	time = Label(bill, text = "start time must be before end time").grid(sticky = "w",row = 3, column = 0)



#Dictionaries for Dropdown menu
#contains predefined times
sTList= ["5p","6p", "7p", "8p", "9p", "10p", "11p", "12p","1a", "2a", "3a" ]
eTList = ["6p", "7p", "8p", "9p", "10p", "11p", "12p","1a", "2a", "3a", "4a" ]
bTList = ["5p","6p", "7p", "8p", "9p", "10p", "11p", "12p","1a", "2a", "3a", "4a"]

################# Drop Down Menus#####################
#Set start time variable to 5p by default
stimevar = StringVar(root)
stimevar.set("5p")

#Start time menu 
stimeMenu = OptionMenu(root, stimevar, *sTList)
Label(root, text = "Start Time").grid(sticky ="w", row = 1, column = 1)
stimeMenu.grid(row = 1, column = 2)

#set end time variable to 6p by default
etimevar = StringVar(root)
etimevar.set("6p")

#End time menu
etimeMenu = OptionMenu(root, etimevar, *eTList)
Label(root, text = "End Time").grid(sticky ="w", row = 2, column = 1)
etimeMenu.grid(row =2, column = 2)

#set bed time variable to 5p by default
btimevar = StringVar(root)
btimevar.set("5p")

#Bed Time Menu
btimeMenu = OptionMenu(root, btimevar, *bTList)
Label(root, text = "Bed Time").grid(sticky ="w", row = 3, column = 1)
btimeMenu.grid(row = 3, column = 2)

#Add Button to Calculate Charge
Label(root, text = "Calculate Pay").grid(row = 4, column = 1)
cpay = Button(root, text = "go", width = 6, command = calculateBill).grid(row = 4, column =2)


#starts main window
root.mainloop()