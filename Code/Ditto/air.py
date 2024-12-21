import requests
import json

# Define the URL of your Ditto instance for creating the specific thing
thing_id = "org.eclipse.ditto:air-quality-management_001"
ditto_url = f"http://localhost:8080/api/2/things/{thing_id}"

# Define authentication credentials
username = "ditto"
password = "ditto"

# Define the payload for creating the air quality management thing
payload = {
    "thingId": thing_id,
    "policyId": "org.eclipse.ditto:example_policy_001",
    "definition": "org.eclipse.ditto:AirQualityManagementModel:1.0.0",
    "attributes": {
        "location": {
            "latitude": 44.673856,
            "longitude": 8.261719
        }
    },
    "features": {
        "co2_sensor": {
            "properties": {
                "co2_level": 400,
                "unit": "ppm"
            }
        },
        "oxygen_sensor": {
            "properties": {
                "oxygen_level": 20.95,
                "unit": "percentage"
            }
        },
        "pm25_sensor": {
            "properties": {
                "pm25_level": 12,
                "unit": "µg/m³"
            }
        },
        "pm10_sensor": {
            "properties": {
                "pm10_level": 20,
                "unit": "µg/m³"
            }
        },
        "temperature_sensor": {
            "properties": {
                "temperature": 22,
                "unit": "°C"
            }
        },
        "humidity_sensor": {
            "properties": {
                "humidity": 45,
                "unit": "percentage"
            }
        },
        "voc_sensor": {
            "properties": {
                "voc_level": 200,
                "unit": "ppb"
            }
        },
        "no2_sensor": {
            "properties": {
                "no2_level": 0.02,
                "unit": "ppm"
            }
        },
        "so2_sensor": {
            "properties": {
                "so2_level": 0.01,
                "unit": "ppm"
            }
        },
        "co_sensor": {
            "properties": {
                "co_level": 0.9,
                "unit": "ppm"
            }
        }
    }
}

# Send the PUT request to create the air quality management thing with authentication
response = requests.put(ditto_url, json=payload, auth=(username, password))

# Print the response status code and content
print("Response Status Code:", response.status_code)
print("Response Content:", response.text)
