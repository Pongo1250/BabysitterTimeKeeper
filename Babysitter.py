# Babysitter.py

#time is entered through input in GUI dropdown menu

def inputStartTime(rawStartTime):
	#runs input  for start time
	#will run sub processes here for start time 
	return rawStartTime


###FIXME##### 
#this will run in gui after time and bed check
#must modify am times for math by increasing value by 12
def timeSplit(rawStartTime):
	#this function splits the inputed string into a start time integer
	#and an am/pm indicator string
	#The values then get stored in a list for later use. 
	timeInt = rawStartTime[0:-1]
	timeInt = int(timeInt)
	DayStr = rawStartTime[-1:]

	#converting am times to miliatry time
	if (DayStr == "a"):
		timeInt = timeInt + 12
	li = [timeInt, DayStr]
	return li

def timeCheck(rawStartTime, rawEndTime):
	#This function verifies that start time is before end time

	#Split raw times into time and am/pm indicator
	#start time split

	stimeInt = rawStartTime[0:-1]
	stimeInt = int(stimeInt)
	sDayStr = rawStartTime[-1:]
	#end time split
	etimeInt = rawEndTime[0:-1]
	etimeInt = int(etimeInt)
	eDayStr = rawEndTime[-1:]

	if(sDayStr == "p"):
		if(eDayStr == "a"):
			return "true"
		if(eDayStr == "p"):
			if(stimeInt < etimeInt):
				return "true"
			else:
				return "false"
	if (sDayStr == "a"):
		if (eDayStr == "p"):
			return "false"
		if (eDayStr == "a"):
			if(stimeInt < etimeInt):
				return "true"
			else:
				return "false"


def bedCheck(rawStartTime, rawEndTime, rawBedTime):
	#This function verifies that bed time falls between
	# start time and end time

	#Split raw times into time and am/pm indicator
	#start time split
	stimeInt = rawStartTime[0:-1]
	stimeInt = int(stimeInt)
	sDayStr = rawStartTime[-1:]
	#end time split
	etimeInt = rawEndTime[0:-1]
	etimeInt = int(etimeInt)
	eDayStr = rawEndTime[-1:]
	#bed time split
	btimeInt = rawBedTime[0:-1]
	btimeInt = int(btimeInt)
	bDayStr = rawBedTime[-1:]

	if (sDayStr == "p"):
		if(eDayStr == "p"):
			if(bDayStr == "a"):
				return "false"
			if(btimeInt>= stimeInt):
				if(btimeInt<= etimeInt):
					return "true"
				else:
					return "false"
			else:
				return "false"
		if(eDayStr == "a"):
			if(bDayStr == "p"):
				if(btimeInt >= stimeInt):
					return "true"
				else:
					return "false"
			if(bDayStr == "a"):
				if (btimeInt <= etimeInt):
					return "true"
				else: 
					return "false"
	#checks that bedtime is between or equal to morning times
	if(sDayStr =="a"):
		if(eDayStr == "a"):
			if(bDayStr == "p"):
				return "false"
			if(btimeInt >= stimeInt):
				if(btimeInt <= etimeInt):
					return "true"
				else:
					return "false"
			else:
				return "false"
		else:
			return "false"



def SToBPay(stime, btime):
	Ttime = btime - stime
	Total = Ttime * 12
	return Total


