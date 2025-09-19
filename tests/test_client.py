import pytest
from unittest.mock import patch, Mock
import requests
from src.client.client import Client
from src.errors.http import HttpError

@pytest.fixture
def client():
    return Client("https://api.example.com/v1", "abc123")

# test base_url, host stuffs

@patch('src.client.client.requests.get')
def test_models(mock_get, client):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "data": [
            {"id": "🐡"},
            {"id": "🥕"}
        ]
    }
    mock_get.return_value = mock_response
    assert client.models() == ["🐡", "🥕"]

@patch('src.client.client.requests.get')
def test_http_errors(mock_get, client):
    """Test that HttpError is raised correctly for different status codes"""
    
    # Create a mock response
    mock_response = Mock()
    mock_get.return_value = mock_response
    
    # Test each error code in HttpError.ERROR_MESSAGES
    for status_code, expected_message in HttpError.ERROR_MESSAGES.items():
        # Configure the mock response for this status code
        mock_response.status_code = status_code
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError()
        
        # Call the client method and check that the correct error is raised
        with pytest.raises(HttpError) as excinfo:
            client.request("/test")
            
        # Verify the error details
        assert excinfo.value.status_code == status_code
        assert excinfo.value.message == expected_message
        assert str(excinfo.value) == f"HTTP Error {status_code}: {expected_message}"
        