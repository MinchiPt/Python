import requests

def get_weather(city, units='metric', api_key='<api-key>'):
    #https://api.openweathermap.org/data/2.5/weather?appid=<api-key>&units=metric
    #https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
    #https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
  url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"
  r = requests.get(url)
  content = r.json()
  print(content)
  return content['clouds'], content['main']['temp'], content['weather'][0]['description']
  #print(f"{content['clouds']}, {content['main']['temp']}, {content['weather'][0]['description']}\n"
  # )
  #with open('data.txt', 'a') as file:      
    #for dicty in content['list']:
      #print(f"{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n")
      #file.write(f"{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n")

print('Macau: ', get_weather(city='Macao'))
