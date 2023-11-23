import json

import requests

url = "https://cdn.jsdelivr.net/npm/primeng@9.0.5/resources/themes/nova-light/fonts/open-sans-v15-latin-regular.woff2"

response = requests.get(url)
# print(response)
response_json=response.json
print(response_json)

# r_sc=response.status_code
# print(r_sc)
