import requests

def get_news(topic, from_date, to_date, language='en', api_key='3cdac0182a7f40afb1c4d10bfacf9230'):
#https://newsapi.org/v2/everything?q=Apple&from=2023-01-15&sortBy=popularity&apiKey=API_KE
  url = f'https://newsapi.org/v2/everything?q={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
  r = requests.get(url)
  content = r.json()
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")
  return results

# NOTE: Change the from_date and to_date below to reflect recent dates
# Otherwise, you will get an error.
print(get_news(topic='Apple', from_date='2023-01-01', to_date='2023-01-15'))
