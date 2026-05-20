import behave

from pages.contact_page import ContactPage

@behave.given('valid contact form data')
def step_valid_contact_form_data(context):
    context.valid_contact_form_data = {
        'first_name': 'Hoo',
        'last_name': 'Lee Sheet',
        'email': 'hoolee.sheet@chingbong.com',
        'subject': 'Payments',
        'message': 'Czy mogę płacić wientamskimi dongami? Nie mam innej waluty a potrzebuję thor hammer, koniecznie na jutro. Proszę o odpowiedź to dla mnie ważne',
    }

@behave.given('invalid contact form data')
def step_invalid_contact_form_data(context):
    context.invalid_contact_form_data = {
        'first_name': 'Hoo',
        'last_name': 'Lee Sheet',
        'email': 'leesin_testing.xiu',
        'subject': 'Payments',
        'message': 'Czy mogę płacić wientamskimi dongami? Nie mam innej waluty a potrzebuję thor hammer, koniecznie na jutro. Proszę o odpowiedź to dla mnie ważne',
    }

@behave.given('missing contact form data')
def step_missing_contact_form_data(context):
    context.missing_contact_form_data = {
        'first_name': 'Hoo',
        'last_name': 'Lee Sheet',
        'subject': 'Payments',
        'message': 'Czy mogę płacić wientamskimi dongami? Nie mam innej waluty a potrzebuję thor hammer, koniecznie na jutro. Proszę o odpowiedź to dla mnie ważne',
    }

@behave.when('user opens contact form page')
def step_open_contact_page(context):
    context.page = ContactPage(context.driver)
    context.page.open()

@behave.when('user inputs valid contact form data')
def step_input_valid_contact_data(context):
    context.page.input_form_data(context.valid_contact_form_data)

@behave.when('user inputs invalid contact form data')
def step_input_valid_contact_data(context):
    context.page.input_form_data(context.invalid_contact_form_data)

@behave.when('user inputs missing contact form data')
def step_input_missing_contact_data(context):
    context.page.input_form_data(context.missing_contact_form_data)

@behave.when('user submits message')
def step_submit_message(context):
    context.page.submit()

@behave.then('contact message is sent')
def step_contact_message_sent(context):
    assert context.page.message_sent()

@behave.then('invalid email error is displayed')
def step_invalid_email_error_displayed(context):
    assert context.page.invalid_email_error_displayed()