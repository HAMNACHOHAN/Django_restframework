import requests


url = "https://reqres.in/api/users/2"

response = requests.delete(url)

# Fetch response code

print(response.status_code)

# for validation
assert response.status_code == 204
