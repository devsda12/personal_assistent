import requests

response = requests.get("http://127.0.0.1:5000/lol")
print(response.content)

response = requests.get("http://127.0.0.1:5000/lol?id=lolzo")
print(response.content)