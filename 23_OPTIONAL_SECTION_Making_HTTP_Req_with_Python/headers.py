import requests
url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "application/json"})
# other options for "Accept" could be, "text/plain", "text/html"

data = response.json()	# response comes as a string of json, so you have to convert string into dictionary of json.

# print(type(data) : it is dictionary

print(data["joke"])
print(f"status: {data['status']}")	# it prints the status of response.



