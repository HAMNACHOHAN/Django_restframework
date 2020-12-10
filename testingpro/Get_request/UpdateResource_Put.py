import requests
import json
import jsonpath
# Api Url
url = "https://reqres.in/api/users/2"

# Read input json file
file = open('C:\\Users\\AJ TEch\\PycharmProjects\\testingpro\\create_user.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

# print(request_json) #able to read request

 #make Put  request with json input body
response = requests.put(url, request_json)
print(response.content)

#validating response code
assert response.status_code == 200

# response_json =json.loads(response.text)
# updated_li = jsonpath.jsonpath(response_json, 'updatedAt')
# print(updated_li[0])

