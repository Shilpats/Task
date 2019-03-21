"""
Testcase to Search for a keyword in se
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os,sys,time

class Action():
    """
    Testcase_ui
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
        url='https://duckduckgo.com'
        search_text='relayr'
        browser = webdriver.Chrome(executable_path='E:\chromedriver.exe')
        time.sleep(3)
        browser.maximize_window()
        browser.get(url)
        time.sleep(2)
        inputElement = browser.find_element_by_id('search_form_input_homepage')
        inputElement.send_keys(search_text)
        inputElement.submit()
        time.sleep(10)
        text=browser.find_element_by_id('search_form_input').get_attribute("value")
        if text==search_text:
            print "Same text is present in search box in the search result page"
        else:
            print "Different text : %s is present in search box"%text
        results = browser.find_elements_by_class_name('result')
        for i in range(len(results)-1):
            if 'relayr' in results[i].text:
                print 'Search results displayed is relevant to the search keyword'
            else:
                print 'irrelevant results are displayed'
        browser.close()
        browser.quit()

    
if __name__ == "__main__":
    TEST1 = Action()        
