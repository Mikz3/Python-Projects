import unittest
from Coffee_menu import CoffeeMenu

class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
      self.menu = CoffeeMenu()
    
    # Testing Assertions
    # Test if the price of an existing item (e.g, "latte")
    def test_get_price_exisiting_item(self):
       self.assertEqual(self.menu.get_price("latte"), 2.75)
    
    # Test if a non-existing item returns Non
    def test_get_price_non_existing_item(self):
       self.assertIsNone(self.menu.get_price("mocha"))

    # Test to see if we can successfully add a new item to the menu
    def test_add_item(self):
       self.menu.add_item(("latte"), 2.75)
       self.assertEqual(self.menu("latte"), 2.75)
    
    # Clean up (if necessary) after each test
    def tearDown(self):
       pass
    
# Running the tests
if __name__ == "__main__":
   unittest.main

