import requests

uri = "https://reqres.in/api/users"


def test_api():
    response = requests.get(uri)
    print(response.json())
    json_data = response.json()
    print(json_data['data'][0]['email'])
