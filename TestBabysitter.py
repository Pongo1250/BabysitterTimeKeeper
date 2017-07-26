# TestBabysitter.py

#import statements
import unittest
import Babysitter

class TimeValues(unittest.TestCase):
	#unittest formula is
	#test_functionName_testDescription

	#test function receives a string and retuns an int and a str
	#
	def test_inputStartTime_testInput(self):
		#capture results of function
		result = Babysitter.inputStartTime("500a")
		#check for expected output
		expected = "500a"
		self.assertEqual(expected, result)



	####timeSplit tests
	def test_timeSplit_dayCheck(self):
		timeint = Babysitter.timeSplit("1a")
		expectedInt = 13
		self.assertEqual(expectedInt, timeint)
	def test_timeSplit_nightCheck(self):
		timeint = Babysitter.timeSplit("5p")
		expectedInt = 5
		self.assertEqual(expectedInt, timeint)


	###timeCheck tests
	#test should return true
	def test_timeCheck_paCheck(self):
		stime = "5p"
		etime = "1a"
		testValue = Babysitter.timeCheck(stime,etime)
		expected = "true"
		self.assertEqual(expected,testValue) 
	#test should return true
	def test_timeCheck_ppCheckT(self):
		stime = "5p"
		etime = "6p"
		testValue = Babysitter.timeCheck(stime,etime)
		expected = "true"
		self.assertEqual(expected, testValue)
	#tests that etime and stime are the same should return false
	def test_timeCheck_ppCheckSame(self):
		stime = "6p"
		etime = "6p"
		testValue = Babysitter.timeCheck(stime, etime)
		expected = "false"
		self.assertEqual(expected, testValue)
	#this test checks that a start time after the end time returns false
	def test_timeCheck_ppCheckAfter(self):
		stime = "6p"
		etime = "5p"
		testValue = Babysitter.timeCheck(stime, etime)
		expected = "false"
		self.assertEqual(expected, testValue)
	#tests that a etime before stime returns false
	def test_timeCheck_apCheck(self):
		stime = "1a"
		etime = "6p"
		testValue = Babysitter.timeCheck(stime, etime)
		expected = "false"
		self.assertEqual(expected, testValue)
	#this test should return true. 
	def test_timeCheck_aaCheckT(self):
		stime = "1a"
		etime = "4a"
		testValue = Babysitter.timeCheck(stime, etime)
		expected = "true"
		self.assertEqual(expected, testValue)
	#this test checks that the same start and end time returns false
	def test_timeCheck_aaCheckSame(self):
		stime = "2a"
		etime = "2a"
		testValue = Babysitter.timeCheck(stime, etime)
		expected = "false"
		self.assertEqual(expected, testValue)
	#test checks that a start time after and end time returns false
	def test_timeCheck_aaCheckAfter(self):
		stime = "4a"
		etime = "2a"
		testValue = Babysitter.timeCheck(stime, etime)
		expected = "false"
		self.assertEqual(expected, testValue)

	###bedCheck tests

	##tests night time values
	#test should return true for bed time between s and e time
	def test_bedCheck_ppCheckbetween(self):
		stime = "5p"
		etime = "9p"
		btime = "6p"
		testValue = Babysitter.bedCheck(stime, etime, btime)
		expected = "true"
		self.assertEqual(expected, testValue)
	#test same start and bed time. should retun true
	def test_bedCheck_ppCheckStart(self):
		stime = "5p"
		etime = "9p"
		btime = "5p"
		testValue = Babysitter.bedCheck(stime, etime, btime)
		expected = "true"
		self.assertEqual(expected, testValue)
	#test same end and bed time. should return true
	def test_bedCheck_ppCheckEnd(self):
		stime = "5p"
		etime = "9p"
		btime = "9p"
		testValue = Babysitter.bedCheck(stime, etime, btime)
		expected = "true"
		self.assertEqual(expected, testValue)
	#tests that bedtime before start time returns false
	def test_bedCheck_ppCheckBefore(self):
		stime = "7p"
		etime = "9p"
		btime = "6p"
		testValue = Babysitter.bedCheck(stime, etime, btime)
		expected = "false"
		self.assertEqual(expected, testValue)
	#tests that bed time after end time returns false
	def test_bedCheck_ppCheckAfter(self):
		stime = "7p"
		etime = "9p"
		btime = "10p"
		testValue = Babysitter.bedCheck(stime, etime, btime)
		expected = "false"
		self.assertEqual(expected, testValue)
	#tests that bed time in the morning with end time at night returns false
	def test_bedCheck_ppCheckMorning(self):
		stime = "7p"
		etime = "9p"
		btime = "1a"
		testValue = Babysitter.bedCheck(stime, etime, btime)
		expected = "false"
		self.assertEqual(expected, testValue)

	## checks bed time between night start time and day end time
	#test should return true for bed time between start and end time
	def test_bedCheck_paCheckBetweenp(self):
		stime = "7p"
		etime = "3a"
		btime = "9p"
		testValue = Babysitter.bedCheck(stime, etime, btime)
		expected = "true"
		self.assertEqual(expected, testValue)
	def test_bedCheck_paCheckBetweena(self):
		stime = "7p"
		etime = "3a"
		btime = "1a"
		testValue = Babysitter.bedCheck(stime, etime, btime)
		expected = "true"
		self.assertEqual(expected, testValue)
	#test should return true for same bed and end time
	def test_bedCheck_paCheckSameE(self):
		stime = "7p"
		etime = "3a"
		btime = "3a"
		testValue = Babysitter.bedCheck(stime, etime, btime)
		expected = "true"
		self.assertEqual(expected, testValue)
	def test_bedCheck_paCheckSameS(self):
		stime = "7p"
		etime = "3a"
		btime = "7p"
		testValue = Babysitter.bedCheck(stime, etime, btime)
		expected = "true"
		self.assertEqual(expected, testValue)
	#test should return false for btime before stime
	def test_bedCheck_paCheckBefore(self):
		stime = "7p"
		etime = "3a"
		btime = "5p"
		testValue = Babysitter.bedCheck(stime, etime, btime)
		expected = "false"
		self.assertEqual(expected, testValue)
	#test should return false for btime after etime
	def test_bedCheck_paCheckAfter(self):
		stime = "7p"
		etime = "3a"
		btime = "4a"
		testValue = Babysitter.bedCheck(stime, etime, btime)
		expected = "false"
		self.assertEqual(expected, testValue)

	##test morning times
	#test should return true if btime between s and e time
	def test_bedCheck_aaCheckBetween(self):
		stime = "1a"
		etime = "3a"
		btime = "2a"
		testValue = Babysitter.bedCheck(stime, etime, btime)
		expected = "true"
		self.assertEqual(expected, testValue)
	#test should return true if btime and stime are the same
	def test_bedCheck_aaCheckSameS(self):
		stime = "1a"
		etime = "3a"
		btime = "1a"
		testValue = Babysitter.bedCheck(stime, etime, btime)
		expected = "true"
		self.assertEqual(expected, testValue)
	#test should return true if btime and etime are the same
	def test_bedCheck_aaCheckSameE(self):
		stime = "1a"
		etime = "3a"
		btime = "3a"
		testValue = Babysitter.bedCheck(stime, etime, btime)
		expected = "true"
		self.assertEqual(expected, testValue)
	#test should return false if btime is pm nd stime is am
	def test_bedCheck_aaCheckBeforeP(self):
		stime = "1a"
		etime = "3a"
		btime = "5p"
		testValue = Babysitter.bedCheck(stime, etime, btime)
		expected = "false"
		self.assertEqual(expected, testValue)
	#test should return false if btime is after etime
	def test_bedCheck_aaCheckAfterE(self):
		stime = "1a"
		etime = "3a"
		btime = "4a"
		testValue = Babysitter.bedCheck(stime, etime, btime)
		expected = "false"
		self.assertEqual(expected, testValue)

	###test SToBPay
	#test same start and bed time equals 0
	def test_SToBPay_Same(self):
		stime = 5
		btime = 5
		testValue = Babysitter.SToBPay(stime, btime)
		expected = 0
		self.assertEqual(expected, testValue)
	#test a small value
	def test_SToBPay_SmallVal(self):
		stime = 5
		btime = 7
		testValue = Babysitter.SToBPay(stime,btime)
		expected = 24
		self.assertEqual(expected, testValue)
	#test big value
	def test_SToBPay_BigVal(self):
		stime = 5
		btime = 16
		testValue = Babysitter.SToBPay(stime, btime)
		expected = 132
		self.assertEqual(expected, testValue)

	###test BToMPay
	#test bed time at midnight equals 0
	def test_BToMPay_Same(self):
		etime = 16
		btime = 12
		testValue = Babysitter.BToMPay(btime, etime)
		expected = 0
		self.assertEqual(expected, testValue)
	#test should return 0 if bed time is greater than midnight
	def test_BToMPay_Greater(self):
		etime = 16
		btime = 16
		testValue = Babysitter.BToMPay(btime, etime)
		expected = 0
		self.assertEqual(expected, testValue)
	#test should return 48
	def test_BToMPay_Before(self):
		etime = 16
		btime = 6
		testValue = Babysitter.BToMPay(btime, etime)
		expected = 48
		self.assertEqual(expected, testValue)
	#test if etime before 12 should return 8
	def test_BToMPay_ETimeBefore(self):
		etime = 7
		btime = 6
		testValue = Babysitter.BToMPay(btime, etime)
		expected = 8
		self.assertEqual(expected, testValue)

	###Test MToEPay
	#test should return 0 if end time is 12
	def test_MToEPay_Same(self):
		etime = 12
		testValue = Babysitter.MToEPay(etime)
		expected = 0
		self.assertEqual(expected, testValue)
	#test should return 0 if end time is before 12
	def test_MToEPay_Before(self):
		etime = 7
		testValue = Babysitter.MToEPay(etime)
		expected = 0
		self.assertEqual(expected, testValue)
	#test should return 16
	def test_MToEPay_Sval(self):
		etime = 13
		testValue = Babysitter.MToEPay(etime)
		expected = 16
		self.assertEqual(expected, testValue)
	#Test should return 64
	def test_MToEPay_Sval(self):
		etime = 16
		testValue = Babysitter.MToEPay(etime)
		expected = 64
		self.assertEqual(expected, testValue)


if __name__ == '__main__':
	unittest.main()