import unittest
from  lineCode import line_function
import os

# define the unit tests
class my_unit_tests(unittest.TestCase):

        # tests if the csv file has been saved
    def test_csv_file_exists(self):
        self.assertTrue(os.path.isfile('lineCsvFile.csv'))


         #tests if data points saved
    def test_data_saved(self):
        pass

        #tests if data points in x are numeric
    def test_data_numeric(self):
       slope, intercept, r_value, p_value, std_err, x, y = line_function()      
       self.assertTrue(all([isinstance(item, int) for item in x]))

        #tests if data points in y are numeric
    def test_data_numeric(self):
       slope, intercept, r_value, p_value, std_err, x, y = line_function()      
       self.assertTrue(all([isinstance(item, int) for item in y]))

       # tests if slope (1.85) is between 1.80 and 1.90
    def test_correct_slope(self):     
        slope, intercept, r_value, p_value, std_err,  x, y = line_function()
        self.assertTrue( 1.80 <= slope <= 1.90)

        # tests if intercept (1.22) is between 1.20 and 1.30
    def test_correct_intercept(self):     
        slope, intercept, r_value, p_value, std_err,  x, y= line_function()
        self.assertTrue( 1.20 <= intercept <= 1.30)
      
    # run the tests
if __name__ == "__main__":
    unittest.main()

