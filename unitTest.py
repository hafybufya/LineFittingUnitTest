import unittest
from  lineCode import line_function
import os

# define the unit tests
class my_unit_tests(unittest.TestCase):

       # tests if slope (1.85) is between 1.80 and 1.90
    def test_correct_slope(self):     
        slope, intercept, r_value, p_value, std_err = line_function()
        self.assertTrue( 1.80 <= slope <= 1.90)

        # tests if intercept (1.22) is between 1.20 and 1.30
    def test_correct_intercept(self):     
        slope, intercept, r_value, p_value, std_err = line_function()
        self.assertTrue( 1.20 <= intercept <= 1.30)

    def test_csv_file_exists(self):
        self.assertTrue(os.path.isfile('lineCsvFile.csv'))

# run the tests
if __name__ == "__main__":
    unittest.main()

    #not plot the graph when running unit test as a futrher improvement