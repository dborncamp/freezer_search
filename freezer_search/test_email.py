import unittest

from freezer_search.home_depot_searcher import find_home_depot
from freezer_search.send_email import send_email


class MyTestCase(unittest.TestCase):
    def test_something(self):
        freezer_url = "https://www.homedepot.com/mcc-cart/v3/appliance/deliveryAvailability/301652925/zipCode/80020?_=1589151139205"

        results = find_home_depot(freezer_url)

        print(results)

        send_email(results[0][1], "https://www.homedepot.com", "dborncamp@gmail.com")


if __name__ == '__main__':
    unittest.main()
