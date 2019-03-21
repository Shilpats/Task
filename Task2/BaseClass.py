# -------------------------------------------------------------------------------
# Name:        baseclass.py
#
# Purpose:     To define the product level functionality
#
# Author:      Shilpa T S
# -------------------------------------------------------------------------------

import requests
import sys
import logging

class baseaction():
    def __init__(self):
        """
        Init function
        """
        sys.path.append(r'C:\Users\USER\Desktop\shilpa\relayr\test\BaseClass.py')
        
        #function to post GET request
    def get_request(self, url, params=None):
        """
        function to post GET request
        """
        try:
            logging.info("Running GET request for the url : %s with parameters : %s", url, params)
            response = requests.get(url, params)
            logging.info("Status code : %d", response.status_code)
            if response.ok:
                logging.info("url : %s with response : %s", response.url, response.text)
                print "HTTP response is successfull : %s \
with response code : %s "%(response.url, response.status_code)
                flag = True
            else:
                logging.error("Request failed : %s \
with response code : %s", response.url, response.status_code)
                print "error"
                return "Error"
        except Exception as expn:
            logging.error("Exception occurred", exc_info=True)
            print expn
            flag = False
        if flag:
            return response

    
