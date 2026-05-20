import behave

from pages.main_page import MainPage

@behave.given('valid search query')
def step_valid_search_query(context):
    context.valid_search_query = 'Saw'

@behave.when('user opens main page')
def step_open_main_page(context):
    context.page = MainPage(context.driver)
    context.page.open()

@behave.when('user inputs valid search query')
def step_input_valid_search_query(context):
    context.page.input_search_query(context.valid_search_query)

@behave.when('user clicks search button')
def step_click_search_button(context):
    context.page.click_search_button()

@behave.when('user selects products category')
def step_select_products_category(context):
    context.page.select_products_category()

@behave.when('user selects price range')
def step_select_price_range(context):
    context.page.select_price_range()

@behave.then('search query is displayed in results')
def step_search_query_displayed_in_results(context):
    assert context.page.get_results_search_query() == context.valid_search_query

@behave.then('only products containing query are visible')
def step_only_filtered_products_are_visible(context):
    assert context.page.all_search_results_contain_search_query(context.valid_search_query)

@behave.then('only products of category are visible')
def step_only_products_of_category_are_visible(context):
    assert context.page.has_any_products()
    assert context.page.contains_product_with_name('sheet sander')
    assert not context.page.contains_product_with_name('pliers')

@behave.then('only products within price range are visible')
def step_only_products_within_price_range_visible(context):
    assert context.page.all_products_within_price_range()