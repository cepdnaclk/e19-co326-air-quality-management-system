import requests
import json

# Define the URL of your Ditto instance for creating the specific thing
thing_id = "org.eclipse.ditto:sensors_fd763647-44aa-45bc-b824-95fa77126d9b"
ditto_url = f"http://localhost:8080/api/2/things/{thing_id}"

# Define your authentication credentials
username = "ditto"
password = "ditto"

# Define the payload for creating the CO2 sensor thing
payload = {
    "thingId": thing_id,
    "policyId": "org.eclipse.ditto:example_policy_001",
    "definition": "org.eclipse.ditto:SensorsModel:1.0.0",  # Adjust model definition for CO2 sensor
    "attributes": {
        "location": {
            "latitude": 44.673856,
            "longitude": 8.261719
        }
    },
    "features": {
        "co2_sensor": {
            "properties": {
                "co2_level": 0.04,  # Example initial CO2 level (in percentage)
                "unit": "percentage"
            }
        }
    }
}

# Send the PUT request to create the CO2 sensor thing with authentication
response = requests.put(ditto_url, json=payload, auth=(username, password))

# Print the response status code and content
print("Response Status Code:", response.status_code)
print("Response Content:", response.text)
