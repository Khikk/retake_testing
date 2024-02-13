import requests_mock
import requests
import json
import pytest

base_url = 'https://petstore.swagger.io/v2/'
user = {
    'id': 0,
    'username': 'test',
    'firstName': 'Иван',
    'lastName': 'Иванов',
    'email': 'test@yandex.ru',
    'password': '12345678',
    'phone': '+70000000000',
    'userStatus': 0
}

def test_create_new_user(requests_mock):
    # при успешном запросе
    requests_mock.post(base_url + 'user', json={'message': 'User created successfully'}, status_code=200)

    response = requests.post(base_url + 'user', json=user)
    assert response.status_code == 200
    assert response.json()['message'] == 'User created successfully'

    # при запросе с неверными параметрами
    requests_mock.post(base_url + 'user', json={'message': 'Invalid parameters'}, status_code=400)

    response_invalid_params = requests.post(base_url + 'user', json={})
    assert response_invalid_params.status_code == 400
    assert response_invalid_params.json()['message'] == 'Invalid parameters'

    # при запросе с неверными параметрами
    requests_mock.post(base_url + 'user', json={'message': 'Internal server error'}, status_code=500)

    response_invalid_data = requests.post(base_url + 'user', json={'id': float('inf')})
    assert response_invalid_data.status_code == 500
    assert response_invalid_data.json()['message'] == 'Internal server error'

    
@pytest.fixture
def mock_session(requests_mock):
    with requests_mock.Mocker() as m:
        yield m

def test_invalid_params(mock_session):
    # при запросе с недопустимыми параметрами
    requests_mock.post(base_url + 'user', json={'message': 'Invalid parameters'}, status_code=400)

    response_invalid_params = requests.post(base_url + 'user', json={'invalid_param': 'value'})
    assert response_invalid_params.status_code == 400
    assert response_invalid_params.json()['message'] == 'Invalid parameters'


def test_mocked_session(mock_session):
    test_create_new_user(mock_session)

    


