from collections.abc import Mapping
from typing import Any

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

class RegistrationPage:
    URL = 'https://practicesoftwaretesting.com/auth/register'
    URL_SUCCESS = 'https://practicesoftwaretesting.com/auth/login'

    FIRST_NAME = (By.ID, 'first_name')
    LAST_NAME = (By.ID, 'last_name')
    DOB = (By.ID, 'dob')
    COUNTRY = (By.ID, 'country')
    POSTAL_CODE = (By.ID, 'postal_code')
    HOUSE_NUMBER = (By.ID, 'house_number')
    PHONE = (By.ID, 'phone')
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'password')
    STREET = (By.ID, 'street')
    REGISTER_ERROR = (By.XPATH, '//div[@data-test=\'register-error\']')
    GOOGLE_SIGN_IN = (By.CLASS_NAME, 'google-sign-in-button')
    SUBMIT = (By.XPATH, '//button[@data-test=\'register-submit\']')
    
    def __init__(self, driver: Firefox) -> None:
        self.driver = driver

    def open(self) -> None:
        self.driver.get(self.URL)

    def register(self, data: Mapping[str, Any]) -> None:
        self.driver.find_element(*self.FIRST_NAME).send_keys(data['first_name'])
        self.driver.find_element(*self.LAST_NAME).send_keys(data['last_name'])
        self.driver.find_element(*self.DOB).send_keys(data['dob'])
        self.driver.find_element(*self.COUNTRY).send_keys(data['country'])
        self.driver.find_element(*self.POSTAL_CODE).send_keys(data['postal_code'])
        self.driver.find_element(*self.HOUSE_NUMBER).send_keys(data['house_number'])

        WebDriverWait(self.driver, 3.0).until(lambda _driver: len(_driver.find_element(*self.STREET).get_attribute('value')) > 0)

        self.driver.find_element(*self.PHONE).send_keys(data['phone'])
        self.driver.find_element(*self.EMAIL).send_keys(data['email'])
        self.driver.find_element(*self.PASSWORD).send_keys(data['password'])

        self.driver.find_element(*self.SUBMIT).click()
    
    def registration_succeeded(self) -> bool:
        try:
            WebDriverWait(self.driver, 3.0).until(lambda _driver: _driver.current_url == self.URL_SUCCESS)
            return True
        except Exception:
            return False
        
    def registration_failed(self) -> bool:
        try:
            WebDriverWait(self.driver, 3.0).until(visibility_of_element_located(self.REGISTER_ERROR))
            return True
        except Exception:
            return False
