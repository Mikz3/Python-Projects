import unittest
import unexpected

class TestUnexpected(unittest.TestCase):                  # Checking the square root function

# Checking Square Roots
    def test_sqrt(self):
      self.assertEqual(unexpected.get_sqrt(144), 12)      # Validate the function works properly
      
# Checking Negative Numbers
    def test_sqrt_negative_numbers(self):
      with self.assertRaises(ValueError):                 # Checking that the square root of a negative number raises a ValueError
        unexpected.get_sqrt(-1)                           

#Checking Division
    def test_divide(self):
      self.assertEqual(unexpected.divide(144, 12), 12)    # Checking that division works
      
    def test_divide_by_0(self):
      with self.assertRaises(ZeroDivisionError):          
         unexpected.divide(6, 0)                          # Checking that when divided by 0 raises a ZeroDivisionError    

if __name__ == "__main__":
  unittest.main()