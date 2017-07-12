# TestBabysitter.py

#import statements
import unittest
import Babysitter

class TimeValues(unittest.TestCase):
	#unittest formula is
	#test_functionName_testDescription

	def test_inputStartTime_testDescription(self):
		#capture results of function
		result = Babysitter.inputStartTime("500a")
		#check for expected output
		expected = "500a"
		self.assertEqual(expected, result)

if __name__ == '__main__':
	unittest.main()