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

	def test_timeSplit_dayCheck(self):
		timestr = Babysitter.timeSplit("500a")[1]
		timeint = Babysitter.timeSplit("500a")[0]
		expected = "a"
		expectedInt = 500
		self.assertEqual(expected, timestr)
		self.assertEqual(expectedInt, timeint)





if __name__ == '__main__':
	unittest.main()