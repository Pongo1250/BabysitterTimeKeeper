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





