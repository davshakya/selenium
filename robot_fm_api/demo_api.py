# import requests

# uri = "https://reqres.in/api/users"

# response = requests.get(uri)
# print(response.json())
# json_data = response.json()
# print(json_data['data'][0]['email'])

with open("test_demo.txt","r+") as xfile:

    xfile.write("Hello this world")
    a=[line for line in xfile]
    print(a)
    
