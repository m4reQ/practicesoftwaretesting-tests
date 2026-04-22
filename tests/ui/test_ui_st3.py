from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, text_to_be_present_in_element, visibility_of_all_elements_located
from selenium.webdriver.common.action_chains import ActionChains

def test_pt3_1(driver: Firefox):
    driver.get('https://practicesoftwaretesting.com/contact')

    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'first_name'))).send_keys('Hoo')
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'last_name'))).send_keys('Lee Sheet')
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'email'))).send_keys('hoolee.sheet@chingbong.com')
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'subject'))).send_keys('Payments')
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'message'))).send_keys('Czy mogę płacić wientamskimi dongami? Nie mam innej waluty a potrzebuję thor hammer, koniecznie na jutro. Proszę o odpowiedź to dla mnie ważne')
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.XPATH, '//input[@data-test=\'contact-submit\']'))).click()

    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.XPATH, '//div[contains(@class, \'alert-success\')]')))

def test_pt3_2(driver: Firefox):
    driver.get('https://practicesoftwaretesting.com/contact')

    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'first_name'))).send_keys('Hoo')
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'last_name'))).send_keys('Lee Sheet')
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'email'))).send_keys('leesin_testing.xiu')
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'subject'))).send_keys('Payments')
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'message'))).send_keys('Testowa wiadomość zawierająca więcej niż 50 znaków dotycząca wybranego tematu.')
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.XPATH, '//input[@data-test=\'contact-submit\']'))).click()

    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.XPATH, '//div[@data-test=\'email-error\']')))

def test_pt3_3(driver: Firefox):
    driver.get('https://practicesoftwaretesting.com/contact')

    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'first_name'))).send_keys('Hoo')
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'last_name'))).send_keys('Lee Sheet')
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'subject'))).send_keys('Payments')
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'message'))).send_keys('Testowa wiadomość zawierająca więcej niż 50 znaków dotycząca wybranego tematu.')
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.XPATH, '//input[@data-test=\'contact-submit\']'))).click()

    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.XPATH, '//div[@data-test=\'email-error\']')))