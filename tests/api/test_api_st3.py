import requests

def test_pt3_1(admin_user: str):
    send_response = requests.post(
        'https://api.practicesoftwaretesting.com/messages',
        json={
            'name': 'Hoo Lee Sheet',
            'email': 'hoolee.sheet@chingbong.com',
            'subject': 'payments',
            'message': 'Czy mogę płacić wientamskimi dongami? Nie mam innej waluty a potrzebuję thor hammer, koniecznie na jutro. Proszę o odpowiedź to dla mnie ważne'})
    assert send_response.status_code == 200

    retrieve_response = requests.get(
        'https://api.practicesoftwaretesting.com/messages',
        headers={
            'Authorization': f'Bearer {admin_user}',
        })
    assert retrieve_response.status_code == 200

    messages = retrieve_response.json()['data']
    assert len(messages) > 0
    assert any(x['name'] == 'Hoo Lee Sheet' for x in messages)

def test_pt3_2():
    send_response = requests.post(
        'https://api.practicesoftwaretesting.com/messages',
        json={
            'name': 'Hoo Lee Sheet',
            'email': 'leesin_testing.xiu',
            'subject': 'payments',
            'message': 'Testowa wiadomość zawierająca więcej niż 50 znaków dotycząca wybranego tematu.'})
    assert send_response.status_code == 422
    assert send_response.json().get('email') is not None

def test_pt3_3():
    send_response = requests.post(
        'https://api.practicesoftwaretesting.com/messages',
        json={
            'name': 'Umar Naraka',
            'subject': 'payments',
            'message': 'Testowa wiadomość zawierająca więcej niż 50 znaków dotycząca wybranego tematu.'})
    assert send_response.status_code == 422
    assert send_response.json().get('email') is not None