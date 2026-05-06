import requests

def test_pt2_1(shopping_cart: str, product: str):
    # act
    response = requests.post(
        f'https://api.practicesoftwaretesting.com/carts/{shopping_cart}',
        json={
            'product_id': product,
            'quantity': 1,
        })
    
    # assert
    assert response.status_code == 200

    cart_response = requests.get(f'https://api.practicesoftwaretesting.com/carts/{shopping_cart}')
    cart_items = cart_response.json()['cart_items']
    assert any(x['product_id'].lower() == product.lower() for x in cart_items)

def test_pt2_2(shopping_cart: str, product):
    # arrange
    requests.post(
        f'https://api.practicesoftwaretesting.com/carts/{shopping_cart}',
        json={
            'product_id': product,
            'quantity': 1,
        })
    
    # act
    response = requests.delete(f'https://api.practicesoftwaretesting.com/carts/{shopping_cart}/product/{product}')

    # assert
    assert response.status_code == 204

    cart_response = requests.get(f'https://api.practicesoftwaretesting.com/carts/{shopping_cart}')
    cart_items = cart_response.json()['cart_items']

    assert len(cart_items) == 0

def test_pt2_3(shopping_cart: str, product: str):
    # NOTE POST /carts/{cartId} route probably has a bug which results in a wrong error being returned
    
    # act
    response = requests.post(
        f'https://api.practicesoftwaretesting.com/carts/{shopping_cart}',
        json={
            'product_id': product,
            'quantity': -1,
        })
    
    # assert
    assert response.status_code == 422
    assert response.json()['message']['errors'].get('quantity') is not None