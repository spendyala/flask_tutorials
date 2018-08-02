import json
import requests

URL_ENDPOINT = 'http://127.0.0.1:9500'

headers = {'content-type': 'application/json'}
response = requests.post(
    f'{URL_ENDPOINT}/f_to_c_json',
    headers=headers,
    data=json.dumps({'fahrenheit': 1000}))
import ipdb; ipdb.set_trace()
print(response.status_code)
print(response.json())
