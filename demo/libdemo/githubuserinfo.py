import requests

userid = input("Enter github userid :")

response = requests.get(f"https://api.github.com/users/{userid}")
if response.status_code != 200: # Error
    print("Sorry! Could not get details")
    exit()

details = response.json()

print(f"Name        : {details['name']}")
print(f"Company     : {details['company']}")
print(f"Location    : {details['location']}")
print(f"Joined  On  : {details['created_at']}")