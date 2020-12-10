import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)

# print(response.content)
# print(response.headers)

# response in json format

json_response = json.loads(response.text)

# print(json_response)
 #fetch value using json
pages = jsonpath.jsonpath(json_response, 'total_pages')
# print(pages[0])

assert pages[0] == 2