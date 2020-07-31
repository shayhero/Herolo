import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "HeroloHomework"))
from Pages.HomePage import locators
import selenium
from selenium.webdriver.common.by import By
from Pages.HomePage.widgets.ourCustomersWidget import *

from commonCommands import Common
import time

@pytest.mark.usefixtures("test_setup")
class HomePage():

    def __init__(self, driver):
        self.driver = driver

    def navigate_our_customers(self):
        try:
             Common.wait_for_element(self, CustomerWidget.customer_navigator)
             target = self.driver.find_element(*CustomerWidget.customer_navigator)

             self.driver.execute_script("arguments[0].scrollIntoView();", target)
             time.sleep(3)


             for element in self.driver.find_elements_by_xpath("//div[@class='slick-slider customers__Slider-sc-1w1u0ay-4 bSKFKn slick-initialized']//ul[@class='slick-dots']"):
                element.click()

        except Exception as e:
            print(e)
            raise

    def navigate_our_jobs(self):
        try:
            Common.wait_for_element(self, JobsWidget.jobs_root)
            target = self.driver.find_element(*JobsWidget.jobs_root)

            self.driver.execute_script("arguments[0].scrollIntoView();", target)
            Common.wait_for_element(self, JobsWidget.right_arrow)
            self.driver.find_element(*JobsWidget.right_arrow).click()
            time.sleep(2)
            Common.wait_for_element(self, JobsWidget.left_arrow)
            self.driver.find_element(*JobsWidget.left_arrow).click()
            time.sleep(2)
        except Exception as e:
            print(e)
            raise

    def scroll_up(self):
        try:
            self.driver.find_element(*Page.scroll_up_button).click()
            Common.wait_for_element(self, Page.logo)



        except Exception as e:
            print(e)
            raise

    def talk_to_us_test(self):
        try:

            self.driver.find_element(*Page.name_input).send_keys("Dror")
            self.driver.find_element(*Page.company_input).send_keys("Kedem")
            self.driver.find_element(*Page.email_input).send_keys("dror.kedem8@gmail.com")
            self.driver.find_element(*Page.phone_input).send_keys("0539869357")
            self.driver.find_element(*Page.talk_to_us_button).click()
            Common.wait_for_element(self, Page.thank_you_message)

        except Exception as e:
            print(e)
            raise


    def click_whatsapp(self):
        try:

            self.driver.find_element(*Page.whatsapp_button).click()
            self.driver.switch_to.window
            self.driver.switch_to.window(self.driver.window_handles[-1])
            Common.wait_for_element(self, Page.whatsapp_identify)
            self.driver.switch_to.window(self.driver.window_handles[0])

            time.sleep(5)

        except Exception as e:
            print(e)
            raise


    # def homepage_is_displayed(self):
    #     try:
    #         Element = self.driver.find_element(*Main.profile_button).isDisplayed()
    #         print(element)
    #         if Element == True:
    #             pass
    #     except Exception as e:
    #         print(e)
    #
    #
    # def navigate_events_screen(self):
    #     self.driver.find_element(*Main.analytics_button).click()
    #     self.driver.find_element(*Main.events_button).click()
    #     time.sleep(5)
    #
    # def click_welcome(self):
    #     self.driver.find_element(*Main.profile_button).click()
    #
    # def click_logout(self):
    #     self.driver.find_element(*profileboard.logout).click()
       
        