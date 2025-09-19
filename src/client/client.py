import requests
import json
from urllib.parse import urljoin
from src.errors.http import HttpError

class Client:
    def __init__(self,
        base_url:str,
        api_key:str="None",
        timeout:int=10, # in seconds
        https:bool=True,
    ):
        # To play nice with urljoin
        if "://" not in base_url:
            base_url = f"https://{base_url}"
        if base_url[-1] != "/":
            base_url = f"{base_url}/"

        self.base_url = base_url
        self.token = api_key
        self.timeout = timeout

    def request(self, endpoint:str, payload:str=None):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        url = urljoin(self.base_url, endpoint)
        
        try:
            response = requests.get(
                url=url,
                data=payload,
                headers=headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.HTTPError as err:
            raise HttpError(response.status_code, response)
        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"Could not connect to '{url}'")
        except requests.exceptions.Timeout:
            raise TimeoutError(f"Request timed out after {self.timeout} seconds")
        except requests.exceptions.RequestException as err:
            raise Exception(err)
    
    def models(self)->list[str]:
        """Return a list of models available"""
        return [m["id"] for m in self.request("/models")["data"]]