import requests
import json
import base64

ditto_host = "http://localhost:8080"
policy_id = "org.eclipse.ditto:example_policy_001"
username = "ditto"
password = "ditto"

# Encode the credentials
auth_string = f"{username}:{password}"
auth_bytes = auth_string.encode('ascii')
base64_bytes = base64.b64encode(auth_bytes)
base64_string = base64_bytes.decode('ascii')

url = f"{ditto_host}/api/2/policies/{policy_id}"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {base64_string}"
}
payload = {
  "entries": {
    "DEFAULT": {
      "subjects": {
        "{{ request:subjectId }}": {
          "type": "the creator"
        }
      },
      "resources": {
        "policy:/": {
          "grant": [
            "READ",
            "WRITE"
          ],
          "revoke": []
        },
        "thing:/": {
          "grant": [
            "READ",
            "WRITE"
          ],
          "revoke": []
        },
        "message:/": {
          "grant": [
            "READ",
            "WRITE"
          ],
          "revoke": []
        }
      }
    }
  }
}

response = requests.put(url, headers=headers, data=json.dumps(payload))

# Print status code and response content for debugging
print("Status Code:", response.status_code)
print("Response Content:", response.text)

# Attempt to parse JSON response
try:
    print(response.json())
except json.JSONDecodeError as e:
    print("JSON Decode Error:", str(e))
