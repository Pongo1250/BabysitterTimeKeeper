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



	#timeSplit tests
	def test_timeSplit_dayCheck(self):
		timestr = Babysitter.timeSplit("400a")[1]
		timeint = Babysitter.timeSplit("400a")[0]
		expected = "a"
		expectedInt = 400
		self.assertEqual(expected, timestr)
		self.assertEqual(expectedInt, timeint)
	def test_timeSplit_nightCheck(self):
		timestr = Babysitter.timeSplit('500p')[1]
		timeint = Babysitter.timeSplit("500p")[0]
		expected = "p"
		expectedInt = 500
		self.assertEqual(expected, timestr)
		self.assertEqual(expectedInt, timeint)
	def test_timeSplit_LargeNumberCheck(self):
		timestr = Babysitter.timeSplit('1057a')[1]
		timeint = Babysitter.timeSplit('1057a')[0]
		expected = "a"
		expectedInt = 1057
		self.assertEqual(expected, timestr)
		self.assertEqual(expectedInt,timeint)

	#timeCheck tests
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


if __name__ == '__main__':
	unittest.main()