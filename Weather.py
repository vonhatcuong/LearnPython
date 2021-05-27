import requests
api_key = "202fdfbe0c3f15407485f8b6205fb446"
city ="Tokyo"
url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key+"&units=imperial"

request =  requests.get(url)
json = request.json()


description = json.get("weather")[0].get("description")
print("Today's forecast is", description)
temp_min = json.get("main").get("temp_min")
print("The minium teamperature is", temp_min)
temp_max = json.get("main").get("temp_max")
print("The minium teamperature is", temp_max)