from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

def test_pt1_1(driver: Firefox):
    driver.get('https://practicesoftwaretesting.com/auth/register')
    
    WebDriverWait(driver, 3.0).until(visibility_of_element_located((By.ID, 'first_name')))

    driver.find_element(By.ID, 'first_name').send_keys('foo')
    driver.find_element(By.ID, 'last_name').send_keys('bar')
    driver.find_element(By.ID, 'dob').send_keys('2000-01-01')
    driver.find_element(By.ID, 'street').send_keys('test 4/20')
    driver.find_element(By.ID, 'postal_code').send_keys('01-001')
    driver.find_element(By.ID, 'city').send_keys('Łódź')
    driver.find_element(By.ID, 'state').send_keys('test')
    driver.find_element(By.ID, 'country').send_keys('Poland')
    driver.find_element(By.ID, 'phone').send_keys('2137')
    driver.find_element(By.ID, 'email').send_keys('foo@bar.com')
    driver.find_element(By.ID, 'password').send_keys('Poziomka13.')
    driver.find_element(By.XPATH, '//button[@data-test=\'register-submit\']').click()

    WebDriverWait(driver, 3.0).until(lambda _driver: _driver.current_url == 'https://practicesoftwaretesting.com/auth/login')
