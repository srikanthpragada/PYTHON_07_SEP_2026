import requests

longitude = input("Enter Longitude :")
latitude = input("Enter Latitude   :")

response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")
if response.status_code != 200: # Error
    print("Sorry! Could not get details")
    exit()

details = response.json()
print('Temperature :', details['current_weather']['temperature'])