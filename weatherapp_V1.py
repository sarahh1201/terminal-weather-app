import requests 

api_key = "YOUR API KEY" # API key from openweathermap,org

location = input("Location: ")
units = input("Imperial (i) or Metrics (m): ")
while units != "i" and units != 'm':
    units = input("Imperial (i) or Metrics (m): ")
                 
result_c = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}')
result_f = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&appid={api_key}')

if units == 'i': 
    result = result_f
if units == 'm':
    result = result_c

description = f"{result.json()['weather'][0]['main']} - {result.json()['weather'][0]['description']}"

# Tempuratures 
temp = round(result.json()['main']['temp'])
feels_like = round(result.json()['main']['feels_like'])
temp_max = round(result.json()['main']['temp_max'])
temp_min = round(result.json()['main']['temp_min'])

# Additional Information 
country = result.json()['sys']['country']

# The icon stuff was used in another project of mine 
# icon_code = result.json()['weather'][0]['icon'] 
# icon_url = f'http://openweathermap.org/img/wn/{icon_code}.png' 

print(f"\n{location.upper()} - {country}\n{description}\nTemperature: {temp}\nFeels like: {feels_like}\nHigh: {temp_max}\nLow: {temp_min}\n")
