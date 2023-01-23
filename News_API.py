import requests

r = requests.get('https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3cdac0182a7f40afb1c4d10bfacf9230')
content = r.json()
print(content['articles']) 
#[print(content['articles'][0]['title'])