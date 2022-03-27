from dataclasses import fields
import requests 


API_KEY = ""
search_query = "software"
location = "55.85610208036833,-4.259438641204655"
radius = "50000" #in meters


url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&keyword={search_query}&type=establishment&key={API_KEY}"

payload = {}
headers = {}

res = requests.get(url, headers=headers, data=payload)

res.status_code
data = res.json()

results = data['results']


refined_business_list = []

for result in results:

    if result['business_status'] != "OPERATIONAL":
        continue
    relevant_data = {
        "business_status": result['business_status'],
        "name": result['name'],
        "place_id": result['place_id'],
        "types": result['types']
    }

    refined_business_list.append(relevant_data)

print(refined_business_list)