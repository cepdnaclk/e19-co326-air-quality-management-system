
# integration_with_twins.py

# Import necessary libraries
import requests
import json

# Constants for API endpoints and configuration
DITTO_URL = "http://ditto-service.local:8080/api/2/things"
KAFKA_BOOTSTRAP_SERVER = "kafka-service.local:9092"
TELEMETRY_TOPIC = "telemetry/air-quality-project"

# Function to update twin state in Eclipse Ditto
def update_twin_state(thing_id, attributes):
    url = f"{DITTO_URL}/{thing_id}"
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({"attributes": attributes})

    response = requests.put(url, headers=headers, data=payload)

    if response.status_code == 200:
        print(f"Successfully updated twin state for {thing_id}.")
    else:
        print(f"Failed to update twin state: {response.text}")

# Example usage
if __name__ == "__main__":
    sensor_id = "air-quality-sensor1"
    twin_attributes = {"pm2.5": 45, "temperature": 23}
    
    update_twin_state(sensor_id, twin_attributes)
