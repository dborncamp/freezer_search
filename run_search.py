from freezer_search import home_depot_searcher
from freezer_search.send_email import send_email

import time
import logging

receiver = 'dborncamp@gmail.com'
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def search(home_depot_urls):
    """Search the URLs and look for something that is available"""
    found = []

    results = home_depot_searcher.find_home_depot(home_depot_urls)

    for result in results:
        url, item_id, available = result
        if available:
            if result not in found:
                logger.warning("!!!Found something available!!!")
                send_email(item_id, url, receiver)
                found.append(result)


if __name__ == "__main__":
    logger.warning("Starting the search")

    home_depot_urls = [
        "https://www.homedepot.com/mcc-cart/v3/appliance/deliveryAvailability/301652925/zipCode/80020",
        "https://www.homedepot.com/mcc-cart/v3/appliance/deliveryAvailability/301652930/zipCode/80020",
        "https://www.homedepot.com/mcc-cart/v3/appliance/deliveryAvailability/301582304/zipCode/80020",
        "https://www.homedepot.com/mcc-cart/v3/appliance/deliveryAvailability/302905157/zipCode/80020"
    ]

    while True:
        search(home_depot_urls)
        time.sleep(1200)
