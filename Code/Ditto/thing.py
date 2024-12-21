import requests
import json

# Define the URL of your Ditto instance for creating things
ditto_url = "http://localhost:8080/api/2/things"

# Define your authentication credentials
username = "ditto"
password = "ditto"

# Define the payload for creating the O2 sensor thing
payload = {
    "topic": "org.eclipse.ditto/air-quality/things/twin/commands/create",
    "headers": {
        "correlation-id": "<command-correlation-id>"
    },
    "path": "/",
    "value": {
        "thingId": "org.eclipse.ditto:co2-sensor_fd763647-44aa-45bc-b824-95fa77126d9b",
        "policyId": "org.eclipse.ditto:001",
        "definition": "org.eclipse.ditto:O2SensorModel:1.0.0",  # Adjust model definition for O2 sensor
        "attributes": {
            "location": {
                "latitude": 44.673856,
                "longitude": 8.261719
            }
        },
        "features": {
            "xo2_sensor": {
                "properties": {
                    "oxygen_level": 0.21,  # Example initial oxygen level
                    "unit": "percentage"
                }
            }
        }
    }
}

# Send the POST request to create the O2 sensor thing with authentication
response = requests.post(ditto_url, json=payload, auth=(username, password))

# Print the response status code and content
print("Response Status Code:", response.status_code)
print("Response Content:", response.text)
