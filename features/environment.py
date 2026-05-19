from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

def before_scenario(context, scenario):
    options = Options()
    options.add_argument("--headless=new")
    
    context.driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install())) # type: ignore

def after_scenario(context, scenario):
    context.driver.quit()