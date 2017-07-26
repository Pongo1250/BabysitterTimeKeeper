# Babysitter.py

#time must be entered in military time


def inputStartTime(rawStartTime):
	#runs input  for start time
	#will run sub processes here for start time 
	return rawStartTime


def timeSplit(rawStartTime):
	#this function splits the inputed string into a start time integer
	#and an am/pm indicator string
	#The values then get stored in a list for later use. 
	timeInt = rawStartTime[0:-1]
	timeInt = int(timeInt)
	DayStr = rawStartTime[-1:]
	li = [timeInt, DayStr]
	return li




def timeCheck(time, ap):
	#check that time is between 5:00 pm and 4:00 am
	minutes = str(time)[-2:]
	minutes = int(minutes)
	if(time >1259):
		print ("time must be between 000 and 1259")
		return "false"
	elif(time< 0):
		print("time must be between 00 and 1259")
		return "false"
	if (minutes > 59):
		print("minutes must be between 00 and 59")
		return "false"
	return "true"

