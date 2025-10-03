import unittest
from  lineCode import line_function

# define the unit tests
class my_unit_tests(unittest.TestCase):

       # test adding integers
    def test_correct_slope(self):     
        slope, intercept, r_value, p_value, std_err = line_function()
        self.assertTrue( 1.80 <= slope <= 1.90)

    def test_correct_intercept(self):     
        slope, intercept, r_value, p_value, std_err = line_function()
        self.assertTrue( 1.20 <= intercept <= 1.30)

# run the tests
if __name__ == "__main__":
    unittest.main()

    #not plot the graph when running unit test as a futrher improvement