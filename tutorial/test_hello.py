import json
import requests

URL_ENDPOINT = 'http://127.0.0.1:9500'

# Hello World test
print('Testing Hello World')
response = requests.get(URL_ENDPOINT)
print(response.status_code)
print(response.text)
assert response.text == 'Hello World!'
print('\n\n')


# Get Name
print('Testing GET /name/')
response = requests.get(f'{URL_ENDPOINT}/name/subbu')
print(response.status_code)
print(response.text)
assert response.text == 'Hello subbu'
print('\n\n')

# Get f_to_c HELP
print('Testing GET /f_to_c/help')
response = requests.get(f'{URL_ENDPOINT}/f_to_c/help')
print(response.status_code)
print(response.text)
assert response.text == 'Converts Temperatures from Fahrenheit to Celsius'
print('\n\n')

# Get f_to_c Change Fahrenheit
print('Testing GET /f_to_c/help')
response = requests.get(f'{URL_ENDPOINT}/f_to_c/100')
print(response.status_code)
print(response.text)
assert response.text == '37.77777777777778'
print('\n\n')

# POST f_to_c Change Fahrenheit
print('Testing POST /f_to_c/')
response = requests.post(f'{URL_ENDPOINT}/f_to_c/', data="200")
print(response.status_code)
print(response.text)
assert response.text == '93.33333333333333'
print('\n\n')

# POST JSON f_to_c Change Fahrenheit
print('Testing POST JSON /f_to_c_json/')

headers = {'content-type': 'application/json'}
response = requests.post(
    f'{URL_ENDPOINT}/f_to_c_json',
    headers=headers,
    data=json.dumps({'fahrenheit': 1000}))
print(response.status_code)
print(response.json())
assert response.json() == {'celsius': '537.7777777777778'}
print('\n\n')


# POST JSON fs_to_cs Change Fahrenheit
print('Testing POST JSON /fs_to_cs_json/')

headers = {'content-type': 'application/json'}
response = requests.post(
    f'{URL_ENDPOINT}/fs_to_cs_json',
    headers=headers,
    data=json.dumps({'fahrenheits': [10, 20]}))
print(response.status_code)
print(response.json())
assert response.json() == {'celsius': ['-12.222222222222221', '-6.666666666666667']}
print('\n\n')

# POST JSON fs_to_cs EASY Change Fahrenheit
print('Testing POST JSON /fs_to_cs_easy/')

headers = {'content-type': 'application/json'}
response = requests.post(
    f'{URL_ENDPOINT}/fs_to_cs_easy',
    headers=headers,
    data=json.dumps({'fahrenheits': [10, 20]}))
print(response.status_code)
json_response = response.json()
assert json_response == {
  "result": [
    {
      "fahrenheit": 10,
      "celsius": "-12.222222222222221"
    },
    {
      "fahrenheit": 20,
      "celsius": "-6.666666666666667"
    }
  ]
}
print(json.dumps(json_response, indent=2))
