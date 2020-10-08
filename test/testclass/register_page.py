from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from src.testproject.sdk.drivers.webdriver.base import BaseDriver
import time

class RegisterPage:
    url = "https://passport.alibaba.com/member/us/reg/fast/union_reg.htm?_regfrom=ICBU_UNION_REG&_lang=en_US&_regbizsource=main_page&return_url=https%3A%2F%2Fwww.alibaba.com"


    def __init__(self, driver: BaseDriver):
        self._driver = driver

    def open(self):
        self._driver.get(self.url)
        return self

    def register_as(self, country:str, email:str, password:str, company:str, fullname:list, phone:list):
        
        #   Select country
        self._driver.find_element_by_css_selector('.next-select-inner').click()
        self._driver.find_element_by_xpath("//div[@class='next-select-search']//input").send_keys(country)
        time.sleep(3)
        self._driver.find_element_by_css_selector('.next-menu-item').click()

        self._driver.find_element_by_xpath("//input[@value='buyer']").click()

        self._driver.find_element_by_css_selector('#email').send_keys(email)
        self._driver.find_element_by_css_selector('#password').send_keys(password)
        self._driver.find_element_by_css_selector('#rePassword').send_keys(password)
        self._driver.find_element_by_css_selector('#companyName').send_keys(company)
        self._driver.find_element_by_xpath("//input[@name='firstName']").send_keys(fullname[0])
        self._driver.find_element_by_xpath("//input[@name='lastName']").send_keys(fullname[1])
        self._driver.find_element_by_xpath("//input[@name='phoneArea']").send_keys(phone[0])
        self._driver.find_element_by_xpath("//input[@name='phoneNumber']").send_keys(phone[1])

        #       swipe captha
        slider = self._driver.find_element_by_css_selector('.nc_iconfont.btn_slide')
        move = ActionChains(self._driver)
        move.click_and_hold(slider).move_by_offset(400, 0).release().perform()
        #       checkbox verifiacation
        self._driver.find_element_by_xpath("//input[@type='checkbox']").send_keys(Keys.SPACE)

        #       submit
        time.sleep(3)
        self._driver.find_element_by_css_selector(".next-btn.next-btn-primary.next-btn-large.login-btn").click()

    
