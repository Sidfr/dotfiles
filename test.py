import requests

url = "https://greenly.earth/fr-fr/blog/actualites-ecologie/bilan-carbone-entreprise"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
print(response.status_code)