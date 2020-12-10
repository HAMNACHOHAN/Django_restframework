import requests
import json
import jsonpath
# Api Url
url = "https://reqres.in/api/users"

# Read input json file
file = open('C:\\Users\\AJ TEch\\PycharmProjects\\testingpro\\create_user.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)
# print(request_json) #able to read request
#make post request with json input body
response = requests.post(url, request_json)
# print(response.content)

#validating response code
assert response.status_code == 201

#fetch header response
# print(response.headers)
#fetch specific values from header response
print(response.headers.get('Content-Length'))
#fetch response in json format
response_json = json.loads(response.text)
#pick id in json path
id = jsonpath.jsonpath(response_json, 'id')
#it will fetch 1st id from index and just id will print the list of ids
print(id[0])

