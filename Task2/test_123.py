"""
Testcase to post a GET request to find a particular location
"""
import logging
import requests
from BaseClass import baseaction

class Action(baseaction):
    """
    Testcase_123
    """
    def __init__(self):
        """
        Init function
        """
        self.functionality()
    
    def functionality(self):
        """
        test case function
        """
        logging.basicConfig(filename='logs.log', filemode='w', level=logging.DEBUG)
        #Forming the URL to find a particular location by using query argument
        logging.info("Forming the URL to find a particular location using query argument")
        url = "https://www.metaweather.com/api/location/search/"
        location = 'berlin'
        query = ['woeid', 'title', 'latt_long', 'location_type']
        query_params = {'query':location}
        #Posting GET request and verifying the result
        myresponse = self.get_request(url, query_params)
        query_output = myresponse.json()
        for value in enumerate(query_output):
            if set(query) == set(value[1].keys()):
                logging.info("Response : %s has all the required details", myresponse.text)
                print "HTTP response has all the required details"
            else:
                logging.error("Response : %s has missing values", myresponse.text)
                print "HTTP response has missing values"

        #Forming the URL to find a particular location by using lattlong argument
        logging.info("Forming the URL to find a particular location using lattlong argument")
        lat_lon = '52.516071,13.376980'
        latlon_params = {'lattlong': lat_lon}
        latt_long = ['woeid', 'title', 'latt_long', 'location_type', 'distance']
        #Posting GET request and verifying the result
        lattlong = self.get_request(url, latlon_params)
        #output has a list of locations near the co-ordinates lattitude and longitude
        latlon_output = lattlong.json()
        for value in enumerate(latlon_output):
            if set(latt_long) == set(value[1].keys()):
                logging.info("Response %s has all the required details", value[1])
            else:
                logging.error("Response %s has missing values", value[1])
                print "HTTP response has missing values"

if __name__ == "__main__":
    TEST1 = Action()
