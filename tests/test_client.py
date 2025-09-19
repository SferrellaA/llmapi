import pytest
from unittest.mock import patch, Mock
from src.client.client import Client

@pytest.fixture
def client():
    return Client("https://api.example.com/v1", "abc123")

# test base_url, host stuffs

@patch('src.client.client.Client._request')
def test_models(mock_get, client):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "data": [
            {"id": "🐡"},
            {"id": "🥕"}
        ]
    }
    mock_get.return_value = mock_response.json()
    assert client.models() == ["🐡", "🥕"]
        