from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

class CheckoutPage:
    URL = 'https://practicesoftwaretesting.com/checkout'

    def __init__(self, driver: Firefox) -> None:
        self.driver = driver

    def open(self) -> None:
        self.driver.get(self.URL)

    def any_product_present(self) -> bool:
        try:
            WebDriverWait(self.driver, 10.0).until(visibility_of_element_located((By.XPATH, '//span[@data-test=\'product-title\']')))
            return True
        except Exception:
            return False
        
    def any_product_can_be_removed(self) -> bool:
        try:
            WebDriverWait(self.driver, 10.0).until(visibility_of_element_located((By.XPATH, '//span[@data-test=\'product-title\']/../..//a[contains(@class, \'btn\')]')))
            return True
        except Exception:
            return False
        
    def remove_product(self) -> None:
        self.driver.find_element(By.XPATH, '//span[@data-test=\'product-title\']/../..//a[contains(@class, \'btn\')]').click()

    def no_products_present(self) -> bool:
        try:
            WebDriverWait(self.driver, 10.0).until_not(visibility_of_element_located((By.XPATH, '//button[@data-test=\'proceed-1\']')))
            return True
        except Exception:
            return False