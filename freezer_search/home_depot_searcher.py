import requests
import logging

logger = logging.getLogger(__name__)


def find_home_depot(urls):
    """Find out if an appliance is available on the home depot site.

    Returns a list of tuples that contains the URL, itemId, and bool of if it is available  for a given list (or single) urls

    This is home depot specific because their returned json is weird"""
    if isinstance(urls, str):
        urls = [urls]

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

    for i, url in enumerate(urls):
        urls[i] = (url, None, False)

        try:
            r = requests.get(url, headers=headers)
        except Exception as e:
            logger.info(F"Error in looking for {url}")
            logger.info(e)
            continue
        response_json = r.json()

        # If there is "errorData" present, move on
        try:
            a = response_json['DeliveryAvailabilityResponse']["errorData"]
            logger.info(F"Home Depot returned an error on {url} . Response: {a}")
            continue
        except:
            pass

        try:
            available = response_json['DeliveryAvailabilityResponse']['deliveryAvailability']['availability'][0]['status']
            item_id = int(response_json['DeliveryAvailabilityResponse']['deliveryAvailability']['availability'][0]['itemId'])

            urls[i] = (url, item_id, available != "OOS_ETA_UNAVAILABLE")
        except KeyError as e:
            logger.error(F"Problem parsing Home Depot's response on: {url}")
            logger.error(e)

    return urls
