import requests

url = "https://newsapi.org/v2/everything?q=tesla&from=2024-03-24&sortBy=publishedAt&apiKey=6e9f6c8e2d094b4689ae4f070ffa536f"

request = requests.get(url)
content = request.json()

for cont in content["articles"]:
	print(cont["title"])
	print(cont["description"])
	print()