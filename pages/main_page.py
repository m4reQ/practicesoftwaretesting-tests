from selenium.webdriver import ActionChains, Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import WebElement, visibility_of_all_elements_located, visibility_of_element_located


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

    def input_search_query(self, query_text: str) -> None:
        search_query_input: WebElement = WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.ID, 'search-query')))
        search_query_input.send_keys(query_text)

    def click_search_button(self) -> None:
        search_button: WebElement = WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.XPATH, '//button[@data-test=\'search-submit\']')))
        search_button.click()
    
    def get_results_search_query(self) -> str:
        search_term: WebElement = WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.XPATH, '//span[@data-test=\'search-term\']')))
        return search_term.text
    
    def all_search_results_contain_search_query(self, query_text: str) -> bool:
        WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.XPATH, '//div[@data-test=\'search_completed\']')))
    
        product_titles: list[WebElement] = WebDriverWait(self.driver, 3.0).until(visibility_of_all_elements_located((By.XPATH, '//*[@data-test=\'product-name\']')))
        return all(query_text.lower() in x.text.lower() for x in product_titles)
    
    def has_any_products(self) -> bool:
        WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.XPATH, '//div[@data-test=\'filter_completed\']')))

        product_titles: list[WebElement] = WebDriverWait(self.driver, 3.0).until(visibility_of_all_elements_located((By.XPATH, '//*[@data-test=\'product-name\']')))
        return len(product_titles) > 0
    
    def select_price_range(self) -> None:
        price_slider: WebElement = WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.CLASS_NAME, 'ngx-slider-pointer-max')))
        price_slider_bar: WebElement = WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.XPATH, '//span[contains(@class, \'ngx-slider-full-bar\')]')))

        self.driver.execute_script('arguments[0].scrollIntoView();', price_slider)

        ActionChains(self.driver).drag_and_drop_by_offset(
            price_slider,
            -price_slider_bar.rect['width'] / 4,
            0).perform()
        
        self.driver.implicitly_wait(3.0)
        
        max_price_label: WebElement = WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.XPATH, '//span[contains(@class, \'ngx-slider-model-high\')]')))
        self.max_price = int(max_price_label.text.strip())
        
        self.driver.implicitly_wait(3.0)

    def all_products_within_price_range(self) -> bool:
        product_prices: list[WebElement] = WebDriverWait(self.driver, 3.0).until(visibility_of_all_elements_located((By.XPATH, '//*[@data-test=\'product-price\']')))
        return all(float(x.text[1:]) <= self.max_price for x in product_prices)
    
    def select_products_category(self) -> None:
        category_input: WebElement = WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.XPATH, '//label[contains(text(), \'Power Tools\')]/input')))
        category_input.click()
    
    def contains_product_with_name(self, name: str) -> bool:
        WebDriverWait(self.driver, 3.0).until(visibility_of_element_located((By.XPATH, '//div[@data-test=\'filter_completed\']')))

        product_titles: list[WebElement] = WebDriverWait(self.driver, 3.0).until(visibility_of_all_elements_located((By.XPATH, '//*[@data-test=\'product-name\']')))
        return any(name in x.text.lower() for x in product_titles)
