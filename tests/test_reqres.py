import pytest
import requests

BASE_URL = "https://reqres.in/api"


class TestReqResHealth:
    @pytest.mark.smoke
    def test_api_is_reachable(self):
        response = requests.get(f"{BASE_URL}/users?page=1")
        assert response.status_code == 200


class TestReqResUsers:
    @pytest.mark.regression
    def test_list_users(self):
        response = requests.get(f"{BASE_URL}/users?page=1")
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert len(data["data"]) > 0
        assert data["page"] == 1

    @pytest.mark.regression
    def test_get_single_user(self):
        response = requests.get(f"{BASE_URL}/users/2")
        assert response.status_code == 200
        data = response.json()
        assert data["data"]["id"] == 2
        assert "email" in data["data"]
        assert "first_name" in data["data"]

    @pytest.mark.regression
    def test_user_not_found(self):
        response = requests.get(f"{BASE_URL}/users/999")
        assert response.status_code == 404

    @pytest.mark.regression
    def test_create_user(self):
        payload = {"name": "John", "job": "Engineer"}
        response = requests.post(f"{BASE_URL}/users", json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "John"
        assert data["job"] == "Engineer"
        assert "id" in data
        assert "createdAt" in data

    @pytest.mark.regression
    def test_update_user(self):
        payload = {"name": "John Updated", "job": "Manager"}
        response = requests.put(f"{BASE_URL}/users/2", json=payload)
        assert response.status_code == 200
        assert response.json()["name"] == "John Updated"
        assert "updatedAt" in response.json()

    @pytest.mark.regression
    def test_delete_user(self):
        response = requests.delete(f"{BASE_URL}/users/2")
        assert response.status_code == 204


class TestReqResResponseTime:
    @pytest.mark.performance
    def test_list_users_response_time(self):
        response = requests.get(f"{BASE_URL}/users?page=1")
        assert response.elapsed.total_seconds() < 3.0