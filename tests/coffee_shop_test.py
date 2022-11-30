import unittest 
from src.coffee_shop import CoffeeShop

class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self):
        self.coffee_shop_instance = CoffeeShop("McBeans", "It's a great day for a great bean!", 157.00)

    def test_coffee_shop_has_name(self):
        self.assertEqual("McBeans", self.coffee_shop_instance.name)
    
    def test_shop_has_stock(self):
        self.assertEqual(157.00, self.coffee_shop_instance.stock_count)

    def test_say_slogan(self):
        self.assertEqual(None, self.coffee_shop_instance.say_slogan())

    def test_increase_stock_count(self):
        self.coffee_shop_instance.increase_stock_count(3)
        self.assertEqual(160, self.coffee_shop_instance.stock_count)

    def test_coffee_bean_has_full_range(self):
        self.assertEqual(True, self.coffee_shop_instance.has_full_range())