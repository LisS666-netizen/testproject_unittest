import unittest
from src.testproject.decorator import report
from src.testproject.sdk.drivers import webdriver
from testclass import RegisterPage, CheckPage
import time


class PosetivTest(unittest.TestCase):
    @report(
        project='Test Alibaba', job='unittest', test='register test on testproject app',
    )
    def test_register(self):
        driver = webdriver.Firefox()
        RegisterPage(driver).open().register_as("Moldova","vaultshops@gmail.com","287887ee","LegoMD",["Vladimir", "Sergheev"],["","60152032"])
        self.assertIsNotNone(CheckPage(driver).check_error_and_feedback())
        driver.quit()

if __name__ == '__main__':
    unittest.main()