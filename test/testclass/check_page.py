from src.testproject.sdk.drivers.webdriver.base import BaseDriver
import time

class CheckPage:

    def __init__(self, driver:BaseDriver):
        self._driver = driver

    def check_error_and_feedback(self):
        time.sleep(1)
        errors = [i.text for i in self._driver.find_elements_by_css_selector('.next-form-item-explain')]
        return errors

    # def check_feedback(self):
    #     time.sleep(1)
    #     return self._driver.find_element_by_css_selector('.next-feedback').text