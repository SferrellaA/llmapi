from urllib import request
from urllib.error import URLError
import json

endpoint="https://..."
apikey="None"

try:
    response = request.urlopen(endpoint)
    if response.getcode() != 200:
        raise Exception("failed :/")
    response = json.loads(response.read().decode())
    print(response)
except Exception as e:
    print(e)

# TODO - url/header class?
# TODO - better names; make the flow make sense

def stream_request(request):
    for chunk in response:
        yield chunk.decode() #.strip() ?

def request_endpoint(url:str):
    try:
        response = request.urlopen(url)
        if response.getheader('Transfer-Encoding') == 'chunked':
            return stream_request(request)
        return response.read()
    except URLError as e:
        print(e)
    except Exception as e:
        print(e)