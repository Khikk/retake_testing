import requests

def test_successful_request_http_status_code():
    response = requests.post('https://petstore.swagger.io/v2/pet', json={"id": 1, "name": "Rex"})

    assert response.status_code == 200, f"Expected status code 200 for successful request, got {response.status_code}"



    print("Test is successfully!")

test_successful_request_http_status_code()





# import requests

# def test_successful_http_status_code():
#     response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=available")
#     assert response.status_code == 200, "Expected status code 200 for successful request"
