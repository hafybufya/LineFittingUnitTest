# ---------------------------------------------------------------------
# IMPORTED FUNCTIONS USED IN PROGRAM
# ---------------------------------------------------------------------

import unittest
from  mainCode import *
import os
from unittest.mock import patch
from pathlib import Path

# ---------------------------------------------------------------------
# Class of unit tests
# ---------------------------------------------------------------------

class my_unit_tests(unittest.TestCase):

# ---------------------------------------------------------------------
# File handling unit tests
# ---------------------------------------------------------------------

        # tests if the csv file has been saved
    
    def test_csv_file_exists(self):
        self.assertTrue(os.path.isfile(csv_in_use))

       #check code and csv are in the same folder
   
    def test_same_folder(self):
        self.assertTrue(Path(csv_in_use).resolve().parent == Path("mainCode.py").resolve().parent)

# ---------------------------------------------------------------------
# Data checking unit tests
# ---------------------------------------------------------------------

    # Tests if all data points in x are numeric
    @patch("mainCode.plt.show") # Prevents the line plot window from appearing when test is run
    def test_data_numeric_x(self, mockshow):
       
       slope, intercept, x , y = plot_line()      
       self.assertTrue(all([isinstance(item, int) for item in x]))

    # Tests if all data points in y are numeric
    @patch("mainCode.plt.show") # Prevents the line plot window from appearing when test is run
    def test_data_numeric_y(self, mockshow):
       slope, intercept, x, y = plot_line()   
       self.assertTrue(all([isinstance(item, int) for item in y]))
      
    # Checks if there is 2 columns in lineCsvFile
    def test_data_columns(self):
        self.assertTrue(count_columns_pandas(csv_in_use) == 2)

       #checks number of header lines
    # def test_header_number(self):
    #     pass

# ---------------------------------------------------------------------
# Stastics verification unit tests
# ---------------------------------------------------------------------


    #   #checks data is well correlated0.8<
    # def test_correlation():
    #     pass

       # tests if slope (4.07) is between range
    @patch("mainCode.plt.show") # Prevents the line plot window from appearing when test is run
    def test_correct_slope(self, mockshow):     
        slope, intercept, x, y = plot_line()
        self.assertTrue( 4.00 <= slope <= 4.10)

        # tests if intercept (-0.67) is between range
    @patch("mainCode.plt.show") # Prevents the line plot window from appearing when test is run
    def test_correct_intercept(self, mockshow):     
        slope, intercept, x, y = plot_line()
        self.assertTrue( -0.70 <= intercept <= -0.60)
      
    # run the tests
if __name__ == "__main__":
    unittest.main()


# y = 4.07x -0.67