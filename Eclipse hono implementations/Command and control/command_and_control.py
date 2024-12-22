
# command_and_control.py

# Import necessary libraries
import requests
import json

# Constants for API endpoints
HONO_COMMAND_API = "http://{hono-host}:8080/v1/tenants/{tenant_id}/devices/{device_id}/commands"

# Function to send command to IoT device
def send_device_command(tenant_id, device_id, command):
    url = HONO_COMMAND_API.format(tenant_id=tenant_id, device_id=device_id)
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({"command": command})

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        print(f"Command sent successfully to {device_id}: {command}")
    else:
        print(f"Failed to send command: {response.text}")

# Example usage
if __name__ == "__main__":
    tenant_id = "tenant1"
    device_id = "air-quality-sensor1"
    command = "calibrate"

    send_device_command(tenant_id, device_id, command)
