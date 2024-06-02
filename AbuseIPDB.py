import requests
import json

# Replace with your AbuseIPDB API key
api_key = "ab5fb6b4d8828d26e898841a3f43d75117e5578da591a7056b430452e23c49cd415b325aa75f741e"
# IP address to check
ip = "26.0.0.1"

# Set the headers
headers = {
    "Key": api_key,
    "Accept": "application/json"
}

try:
    # Make the request
    response = requests.get(f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}", headers=headers)

    # Check if request was successful
    if response.status_code == 200:
        # Output the response in JSON format
        json_output = json.dumps(response.json(), indent=4)
        print(json_output)
    else:
        print(f"Error: {response.status_code} - {response.text}")
except Exception as e:
    print(f"An error occurred: {e}")
