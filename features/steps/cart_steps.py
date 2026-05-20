import behave

from pages.checkout_page import CheckoutPage
from pages.main_page import MainPage

@behave.when('user opens main page') # type: ignore
def step_open_main_page(context):
    context.page = MainPage(context.driver)
    context.page.open()

@behave.when('items cards are visible') # type: ignore
def step_items_cards_are_visible(context):
    context.page.product_cards_visible()

@behave.when('user clicks on a product card') # type: ignore
def step_user_opens_product_card(context):
    context.page.open_first_product_card()

@behave.when('user clicks add item button') # type: ignore
def step_user_clicks_add_item(context):
    context.page.add_currently_visible_item()

@behave.when('user opens checkout page') # type: ignore
def step_user_opens_checkout_page(context):
    context.page = CheckoutPage(context.driver)
    context.page.open()

@behave.then('products are visible in cart') # type: ignore
def step_products_visible_in_checkout(context):
    assert context.page.any_product_present()

@behave.when('products can be removed') # type: ignore
def step_products_can_be_removed(context):
    assert context.page.any_product_can_be_removed()

@behave.when('user removes product from cart') # type: ignore
def step_remove_product(context):
    context.page.remove_product()

@behave.then('cart is empty') # type: ignore
def step_cart_is_empty(context):
    assert context.page.no_products_present()

@behave.when('user inputs negative quantity') # type: ignore
def step_input_negative_quantity(context):
    context.page.input_item_quantity('-')

@behave.then('quantity is 1') # type: ignore
def step_quantity_is_one(context):
    assert context.page.get_item_quantity() == '1'