import requests

def test_invalid_params_http_status_code():
    response = requests.post('https://petstore.swagger.io/v2/pet/findByStatus', params={'status': 'invalid'})

    assert response.status_code == 400, f"Expected status code 400 for request with invalid parameters, got {response.status_code}"



    print("Test is successfully!")


test_invalid_params_http_status_code()
