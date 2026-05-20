from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import WebElement, visibility_of_element_located


class MainPage:
    URL = 'https://practicesoftwaretesting.com/'

    def __init__(self, driver: Firefox) -> None:
        self.driver = driver

    def open(self) -> None:
        self.driver.get(self.URL)

    def product_cards_visible(self) -> None:
        WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.XPATH, '//div[contains(@class, \'container\') and @data-test]')))

    def open_first_product_card(self) -> None:
        cards_container = self.driver.find_element(By.XPATH, '//div[contains(@class, \'container\') and @data-test]')
        card = cards_container.find_elements(By.CLASS_NAME, 'card')[0]
        card.click()

        WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.ID, 'btn-add-to-cart')))

    def input_item_quantity(self, quantity_text: str) -> None:
        element: WebElement = WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.ID, 'quantity-input')))
        element.clear()
        element.send_keys(quantity_text)

    def get_item_quantity(self) -> str:
        element: WebElement = WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.ID, 'quantity-input')))
        return element.get_attribute('value')

    def add_currently_visible_item(self) -> None:
        self.driver.find_element(By.ID, 'btn-add-to-cart').click()
        WebDriverWait(self.driver, 3.0).until(lambda _driver: len(_driver.find_element(By.ID, 'toast-container').find_elements(By.XPATH, './/*')) > 0)