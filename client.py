from urllib import request
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
