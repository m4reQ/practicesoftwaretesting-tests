from collections.abc import Mapping
from typing import Any

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, new_window_is_opened


class LoginPage:
    URL = 'https://practicesoftwaretesting.com/auth/login'
    GOOGLE_SIGN_IN = (By.CLASS_NAME, 'google-sign-in-button')

    def __init__(self, driver: Firefox) -> None:
        self.driver = driver
        self.old_handles = list[str]()

    def open(self) -> None:
        self.driver.get(self.URL)
        self.old_handles = self.driver.window_handles

    def log_in_using_google(self) -> None:
        WebDriverWait(self.driver, 3.0).until(visibility_of_element_located(self.GOOGLE_SIGN_IN))

        self.driver.find_element(*self.GOOGLE_SIGN_IN).click()
        
    def login_succeeded(self) -> bool:
        try:
            WebDriverWait(self.driver, 3.0).until(new_window_is_opened(self.old_handles))
            return True
        except Exception:
            return False