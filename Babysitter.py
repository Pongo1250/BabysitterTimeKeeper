# Babysitter.py

#time must be entered in military time


def inputStartTime(rawStartTime):
	#runs input  for start time
	if (len(rawStartTime) != 4):
		#wrong satisfies 2nd test
		###FIXME#### add print statement to inform user input is wrong
		return "wrong"
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

def timeIsValid(rawStartTime):
	#verify string formatting is correct
	timeInt = rawStartTime[0:-1]
	DayStr = rawStartTime[-1:]

	#len should be 4. If it is not return wrong
	if (len(rawStartTime) != 4):
		#wrong satisfies 2nd test
		###FIXME#### add print statement to inform user input is wrong
		return "wrong"
	try:
		timeInt = int(timeInt)
	except ValueError:
		return "notNum"
	if (DayStr == 'a'):
		return "true"
	if(DayStr == 'p'):
		return "true"
	return "false"
def timeCheck(time, ap):
	#check that time is between 5:00 pm and 4:00 am
	if(ap == "a"):
		if(time<0):
			return false
		elif(time <=400):
			return "true"
		else:
			return false
