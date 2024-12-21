import requests
import json

# Define the URL of the Ditto API endpoint for updating things
ditto_update_url = "http://localhost:8080/api/2/things/org.eclipse.ditto:fd763647-44aa-45bc-b824-95fa77126d9b"

# Define your authentication credentials
username = "ditto"
password = "ditto"

# Define the new Thing ID
new_thing_id = "org.eclipse.ditto:co2_sensor_001"

# Send a request to retrieve the current information for the Thing
response = requests.get(ditto_update_url, auth=(username, password))

if response.status_code == 200:
    # Retrieve the current information for the Thing
    current_thing_info = response.json()

    # Modify the Thing's information with the new Thing ID
    current_thing_info["thingId"] = new_thing_id

    # Send a request to update the Thing with the modified information
    update_response = requests.put(ditto_update_url, json=current_thing_info, auth=(username, password))

    # Check if the update was successful
    if update_response.status_code == 200:
        print("Thing ID updated successfully.")
    else:
        print("Failed to update Thing ID:", update_response.text)
else:
    print("Failed to retrieve current Thing information:", response.text)
