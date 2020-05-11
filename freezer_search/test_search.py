import unittest

from freezer_search.home_depot_searcher import find_home_depot


class MyTestCase(unittest.TestCase):
    def test_single(self):
        freezer_url = "https://www.homedepot.com/mcc-cart/v3/appliance/deliveryAvailability/301652925/zipCode/80020?_=1589151139205"

        results = find_home_depot(freezer_url)

        print(results)
        self.assertEqual(results[0][0], freezer_url)
        self.assertEqual(type(results[0][1]), int)
        self.assertEqual(type(results[0][2]), bool)


if __name__ == '__main__':
    unittest.main()
