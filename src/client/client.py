import http.client, json

class Client:
    def __init__(self,
        base_url:str,
        api_key:str="None",
        timeout:int=10, # in seconds
        https:bool=True,
    ):
        # cleanup base_url
        if "://" in base_url:
            base_url = base_url.split("://", 1)[1]
        base_url = base_url.rstrip("/")

        # domain vs url
        if "/" in base_url:
            host, self.base_url = base_url.split("/", 1)
            self.base_url = f"/{self.base_url}"
        else:
            host = base_url
            self.base_url = ""
        
        # ssl or not
        if https:
            self.conn = http.client.HTTPSConnection(
                host=host,
                timeout=timeout
            )
        else:
            self.conn = http.client.HTTPConnection(
                host=host,
                timeout=timeout
            )
        
        # api token
        self.token = api_key

    # TODO - how do streaming / chunked responses?
    def _request(self, endpoint:str, payload:str=None):    
        self.conn.request(
            method="GET", 
            url=self.base_url+endpoint,
            body=payload,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            }, 
        )
        response = self.conn.getresponse()

        # TODO - error handling
        if response.status != 200:
            print(response.status)
            raise NotImplementedError
        
        # TODO - error handing
        try:
            return json.loads(response.read())
        except Exception as e:
            print(e)
            raise NotImplementedError
    
    def models(self)->list[str]:
        """Return a list of models available"""
        return [m["id"] for m in self._request("/models")["data"]]

'''      
except requests.exceptions.HTTPError as err:
    if response.status_code == 401:
        print("Authentication failed: Token may be invalid or expired")
    elif response.status_code == 403:
        print("Permission denied: Token does not have access to this resource")
    else:
        print(f"HTTP error occurred: {err}")
except requests.exceptions.ConnectionError:
    print("Connection error: Could not connect to the API")
except requests.exceptions.Timeout:
    print("Timeout error: The request timed out")
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")
'''