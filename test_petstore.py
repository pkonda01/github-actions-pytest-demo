import requests

BASE_URL = "https://petstore.swagger.io/v2"

def test_find_pets_available():
    response = requests.get(f"{BASE_URL}/pet/findByStatus?status=available")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_inventory():
    response = requests.get(f"{BASE_URL}/store/inventory")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_get_pet_by_id():
    response = requests.get(f"{BASE_URL}/pet/1")
    assert response.status_code in [200, 404]

def test_user_not_found():
    response = requests.get(f"{BASE_URL}/user/nonexistent99999")
    assert response.status_code == 404