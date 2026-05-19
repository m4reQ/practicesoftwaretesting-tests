from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def before_scenario(context, scenario):
    options = Options()
    options.add_argument("--headless=new")
    
    context.driver = webdriver.Firefox(options=options)

def after_scenario(context, scenario):
    context.driver.quit()