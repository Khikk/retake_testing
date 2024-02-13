import requests
import json

def test_invalid_params_response_format():
    response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=invalid")
    error_message = response.json()
    assert "message" in error_message, "Expected error message in response for request with invalid parameters"
