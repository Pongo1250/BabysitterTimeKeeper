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


####timeIsValid Tests
	def test_timeIsValid_testInputLen(self):
		result = Babysitter.timeIsValid("500000")
		expected = "wrong"
		self.assertEqual(expected, result)
	def test_timeIsValid_testIsInt(self):
		result = Babysitter.timeIsValid("abcp")
		expected = "notNum"
		self.assertEqual(expected, result)

	def test_timeIsValid_testIsInt(self):
		result = Babysitter.timeIsValid("500l")
		expected = "false"
		self.assertEqual(expected, result)

	def test_timeIsValid_testCorrectInput(self):
		result = Babysitter.timeIsValid("500a")
		expected = "true"
		self.assertEqual(expected, result)
	def test_timeIsValid_testCorrectInput2(self):
		result = Babysitter.timeIsValid("835p")
		expected = "true"
		self.assertEqual(expected, result)



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




if __name__ == '__main__':
	unittest.main()