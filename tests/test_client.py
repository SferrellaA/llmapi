from unittest import TestCase
from unittest.mock import patch, Mock
from src.client.client import Client

class TestClientClass(TestCase):

    @classmethod
    def setUpClass(self):
        self.c = Client("https://api.example.com/v1", "abc123")
    
    # test base_url, host stuffs

    @patch('src.client.client.Client._request')
    def test_models(self, mock_get):

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": [
                {"id": "🐡"},
                {"id": "🥕"}
            ]
        }
        mock_get.return_value = mock_response.json()
        
        #self.assertEqual(self.c._request("/models").json(), ["🐡", "🥕"])
        self.assertEqual(self.c.models(), ["🐡", "🥕"])
        