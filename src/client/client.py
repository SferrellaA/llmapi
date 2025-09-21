import requests
import json
from src.errors.http import HttpError

method_map = {
    "GET": requests.get,
    "POST": requests.post,
    "PUT": requests.put,
    "DELETE": requests.delete,
    "PATCH": requests.patch,
    "HEAD": requests.head,
    "OPTIONS": requests.options
}

class Client:
    def __init__(self,
        base_url:str,
        api_key:str="None",
        timeout:int=10, # in seconds
        model:str=None, # optional
        ca_cert_path:str=None, # path to custom CA certificate bundle
        client_cert:str|tuple[str,str]=None, # path to .pem certificate file or (cert, key) tuple
    ):
        # To play nice with urljoin
        if "://" not in base_url:
            base_url = f"https://{base_url}"
        base_url = base_url.rstrip('/')

        # Basic api info
        self.base_url = base_url
        self.token = api_key
        self.timeout = timeout
        self.model = model

        # Special auth
        self.ca_cert_path = ca_cert_path if ca_cert_path else True
        self.client_cert = client_cert

    def request(self, 
        endpoint:str, 
        method:str="GET",
        payload:str=None
    ):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        url = f"{self.base_url}/{endpoint.lstrip('/')}" # fml urljoin is horrid
       
        try:
            response = method_map[method](
                url=url,
                data=payload,
                headers=headers,
                timeout=self.timeout,
                verify=self.ca_cert_path,
                cert=self.client_cert
            )
            response.raise_for_status()
            return response.json()
        
        # TODO method lookup exceptions
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
        return [m["id"] for m in self.request("/models", "GET")["data"]]
