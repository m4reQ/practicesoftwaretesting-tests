from collections.abc import Mapping
from typing import Any

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, new_window_is_opened

class ContactPage:
    def __init__(self, driver: Firefox) -> None:
        self.driver = driver

    def open(self) -> None:
        self.driver.get('https://practicesoftwaretesting.com/contact')

    def input_form_data(self, data: Mapping[str, Any]) -> None:
        
        WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.ID, 'first_name'))).send_keys(data['first_name'])
        WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.ID, 'last_name'))).send_keys(data['last_name'])
        WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.ID, 'subject'))).send_keys(data['subject'])
        WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.ID, 'message'))).send_keys(data['message'])

        if (email := data.get('email')) is not None:
            WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.ID, 'email'))).send_keys(email)
    
    def submit(self) -> None:
        WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.XPATH, '//input[@data-test=\'contact-submit\']'))).click()

    def message_sent(self) -> bool:
        try:
            WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.XPATH, '//div[contains(@class, \'alert-success\')]')))
            return True
        except Exception:
            return False
        
    def invalid_email_error_displayed(self) -> bool:
        try:
            WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.XPATH, '//div[@data-test=\'email-error\']')))
            return True
        except Exception:
            return False