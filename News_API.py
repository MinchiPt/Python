import requests

r = requests.get('https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=<api-key>')
content = r.json()
print(content['articles']) 
#[print(content['articles'][0]['title'])
