# Babysitter.py

def inputStartTime(rawStartTime):
	#check start time is valid
	#takes a string and seperates it into starrTime int 
	#and string for am/pm
	return rawStartTime


def timeSplit(rawStartTime):
	timeInt = rawStartTime[0:-1]
	timeInt = int(timeInt)
	DayStr = rawStartTime[-1:]

	li = [timeInt, DayStr]

	return li
