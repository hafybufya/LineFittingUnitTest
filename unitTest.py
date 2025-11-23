import unittest
from  mainCode import *
from mainCode import count_columns_pandas
import os

from pathlib import Path

# define the unit tests
class my_unit_tests(unittest.TestCase):

#FILE HANDLING

        # tests if the csv file has been saved
    def test_csv_file_exists(self):
        self.assertTrue(os.path.isfile('lineCsvFile.csv'))

       #check code and csv are in the sam folder
       #UNHARDCODE WHEN WE SHOVE VARIABLE NAMES YH
    def test_same_folder(self):
        self.assertTrue(Path("lineCsvFile.csv").resolve().parent == Path("lineCode.py").resolve().parent)
        
#DATA CHECKING

        #tests if data points in x are numeric
    def test_data_numeric_x(self):
       slope, intercept, x , y = plot_line()      
       self.assertTrue(all([isinstance(item, int) for item in x]))

        #tests if data points in y are numeric
    def test_data_numeric_y(self):
       slope, intercept, r, p, std_err, x , y = plot_line()   
       self.assertTrue(all([isinstance(item, int) for item in y]))
      
       #checks is theres 2 columns
    def test_data_columns(self):
        self.assertTrue(count_columns_pandas("lineCsvFile.csv") == 2)

       #checks number of header lines
    # def test_header_number(self):
    #     pass

#STASTICS VERIFICATION

    #   #checks data is well correlated0.8<
    # def test_correlation():
    #     pass

       # tests if slope (4.07) is between range
    def test_correct_slope(self):     
        slope, intercept, x, y = plot_line()
        self.assertTrue( 4.00 <= slope <= 4.10)

        # tests if intercept (-0.67) is between range
    def test_correct_intercept(self):     
        slope, intercept, x, y = plot_line()
        self.assertTrue( -0.70 <= intercept <= -0.60)
      
    # run the tests
if __name__ == "__main__":
    unittest.main()


# y = 4.07x -0.67