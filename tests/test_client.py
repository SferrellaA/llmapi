import pytest
import requests
from src.client.client import Client
from src.errors.http import HttpError

@pytest.fixture
def client():
    return Client("https://api.example.com/v1", "abc123")

# TODO - test base_url, host stuffs
def test_client(client):
    assert client.base_url == "https://api.example.com/v1"
    assert client.token == "abc123"
    assert client.timeout == 10 # TODO - should this be an environment variable?
    assert client.model == None
    assert client.ca_cert_path == True
    assert client.client_cert == None

def test_models(requests_mock, client):
    requests_mock.get("https://api.example.com/v1/models", json={
        "data": [
            {"id": "🐡"},
            {"id": "🥕"}
        ]
    })
    assert client.models() == ["🐡", "🥕"]

def test_http_errors(requests_mock, client):
    for code, message in HttpError.ERROR_MESSAGES.items():
        requests_mock.get("https://api.example.com/v1/test", status_code=code)
        with pytest.raises(HttpError) as e:
            client.request("/test")
            assert e.value.status_code == status
            assert e.value.message == message
            assert str(e.value) == f"HTTP Error {status_code}: {message}"
