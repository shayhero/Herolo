from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def __init__(self, driver):
    self.driver = driver

class Common:

    def wait_for_element(self, element):
        try:
            myelement = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(element))
            return myelement



        except Exception as e:
            print(e)
            raise
