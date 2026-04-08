import pytest
from selenium.webdriver import Firefox

@pytest.fixture(scope='function')
def driver():
    _driver = Firefox()
    yield _driver

    _driver.quit()