import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


class TestJsonPlaceholderHealth:
    @pytest.mark.smoke
    def test_api_is_reachable(self):
        response = requests.get(f"{BASE_URL}/posts")
        assert response.status_code == 200


class TestPosts:
    @pytest.mark.regression
    def test_list_posts(self):
        response = requests.get(f"{BASE_URL}/posts")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 100

    @pytest.mark.regression
    def test_get_single_post(self):
        response = requests.get(f"{BASE_URL}/posts/1")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        assert "title" in data
        assert "body" in data
        assert "userId" in data

    @pytest.mark.regression
    def test_post_not_found(self):
        response = requests.get(f"{BASE_URL}/posts/9999")
        assert response.status_code == 404

    @pytest.mark.regression
    def test_create_post(self):
        payload = {
            "title": "Test Post",
            "body": "This is a test",
            "userId": 1
        }
        response = requests.post(f"{BASE_URL}/posts", json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Test Post"
        assert "id" in data

    @pytest.mark.regression
    def test_update_post(self):
        payload = {
            "title": "Updated Title",
            "body": "Updated body",
            "userId": 1
        }
        response = requests.put(f"{BASE_URL}/posts/1", json=payload)
        assert response.status_code == 200
        assert response.json()["title"] == "Updated Title"

    @pytest.mark.regression
    def test_delete_post(self):
        response = requests.delete(f"{BASE_URL}/posts/1")
        assert response.status_code == 200


class TestUsers:
    @pytest.mark.regression
    def test_list_users(self):
        response = requests.get(f"{BASE_URL}/users")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 10

    @pytest.mark.regression
    def test_get_single_user(self):
        response = requests.get(f"{BASE_URL}/users/1")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        assert "name" in data
        assert "email" in data


class TestComments:
    @pytest.mark.regression
    def test_get_comments_for_post(self):
        response = requests.get(f"{BASE_URL}/posts/1/comments")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        assert "email" in data[0]


class TestResponseTime:
    @pytest.mark.performance
    def test_response_under_3_seconds(self):
        response = requests.get(f"{BASE_URL}/posts")
        assert response.elapsed.total_seconds() < 3.0