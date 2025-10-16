import unittest
from  lineCode import line_function
import os

# define the unit tests
class my_unit_tests(unittest.TestCase):

#FILE HANDLING

        # tests if the csv file has been saved
    def test_csv_file_exists(self):
        self.assertTrue(os.path.isfile('lineCsvFile.csv'))

       #check code is in right folder
    def code_folder(self):
        pass
      
      #check csv is in right folder
    def csv_folder(self):
        pass

    #check if csv is actually a csv
    def check_csv_is_csv():
        pass

#DATA CHECKING

        #tests if data points in x are numeric
    def test_data_numeric(self):
       slope, intercept, x, y = line_function()      
       self.assertTrue(all([isinstance(item, int) for item in x]))

        #tests if data points in y are numeric
    def test_data_numeric(self):
       slope, intercept, x, y = line_function()   
       self.assertTrue(all([isinstance(item, int) for item in y]))
      
       #checks is theres 2 columns
    def check_data_columns():
        pass

       #checks number of header lines
    def check_header_number():
        pass

#STASTICS VERIFICATION

       #checks number of data points
    def number_data_points():
       pass

      #checks data is well correlated0.8<
    def check_correlation():
        pass

       # tests if slope (4.07) is between range
    def test_correct_slope(self):     
        slope, intercept, x, y = line_function()
        self.assertTrue( 4.00 <= slope <= 4.10)

        # tests if intercept (-0.67) is between range
    def test_correct_intercept(self):     
        slope, intercept, x, y = line_function()
        self.assertTrue( -0.70 <= intercept <= -0.60)
      
    # run the tests
if __name__ == "__main__":
    unittest.main()


# y = 4.07x -0.67