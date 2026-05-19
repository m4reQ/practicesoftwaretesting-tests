import random
import string

import behave

from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage

def random_email() -> str:
    return ''.join(random.choice(string.ascii_letters) for _ in range(8)) + '@gmail.com'

@behave.given('valid registration data') # type: ignore
def step_valid_registration_data(context):
    context.valid_registration_data = {
        'first_name': 'foo',
        'last_name': 'bar',
        'dob': '2000-01-01',
        'country': 'Poland',
        'postal_code': '15-640',
        'house_number': '17',
        'phone': '2137',
        'email': random_email(),
        'password': 'Poziomka13.',
    }

@behave.when('user opens registration page') # type: ignore
def step_open_registration_page(context):
    context.page = RegistrationPage(context.driver)
    context.page.open()

@behave.when('user registers with valid registration data') # type: ignore
def step_input_registration_data(context):
    context.page = RegistrationPage(context.driver)
    context.page.open()

    context.page.register(context.valid_registration_data)

    assert context.page.registration_succeeded()

@behave.then('registration succeeds') # type: ignore
def step_registration_succeeds(context):
    assert context.page.registration_succeeded()

@behave.then('registration fails') # type: ignore
def step_registration_fails(context):
    assert context.page.registration_failed()

@behave.when("user tries to register again with the same data") # type: ignore
def step_register_again(context):
    context.page.open()
    context.page.register(context.valid_registration_data)

@behave.when('user opens login page') # type: ignore
def step_open_login_page(context):
    context.page = LoginPage(context.driver)
    context.page.open()

@behave.when('user logs in using google') # type: ignore
def step_log_in_using_google(context):
    context.page.log_in_using_google()

@behave.then('google account popup shows up') # type: ignore
def step_google_account_popup_visible(context):
    assert context.page.login_succeeded()