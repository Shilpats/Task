"""
Testcase to post a GET request to Source information and forecast history for a particular day & location
"""
import logging
import requests
from datetime import date
from BaseClass import baseaction

class Action(baseaction):
    """
    Testcase_456
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
        logging.basicConfig(filename='log456.log', filemode='w', level=logging.DEBUG)
        #Forming the URL to find a particular location by using query argument
        logging.info("Forming the URL to find a particular location using query argument")
        woeid=44418
        today=date.today()
        d1=today.strftime("%Y/%m/%d")
        url = "https://www.metaweather.com/api/location/%s/%s"%(woeid,d1)
        query = ['wind_speed', 'applicable_date', 'predictability','weather_state_name','created','wind_direction','air_pressure','humidity','visibility','the_temp','min_temp','max_temp','id','weather_state_abbr','wind_direction_compass']
        #Posting GET request and verifying the result
        myresponse = self.get_request(url)
        query_output = myresponse.json()
        for value in enumerate(query_output):
            if set(query) == set(value[1].keys()):
                logging.info("Response : %s has all the required details", myresponse.text)
            else:
                logging.error("Response : %s has missing values", myresponse.text)
                print "HTTP response has missing values"
 

if __name__ == "__main__":
    TEST1 = Action()
    
