# Babysitter.py

def inputStartTime(rawStartTime):
	#check start time is valid
	#takes a string and seperates it into starrTime int 
	#and string for am/pm
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
