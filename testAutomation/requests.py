import requests, json

url = "https://w3schools.com/python/demopage.htm"
response = requests.get(url)
print(response.json())