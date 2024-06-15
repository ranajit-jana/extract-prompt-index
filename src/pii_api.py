import requests
from unique_set import collect_unique_entities

def pii_detection_call(api_url, data):
    #Function to send data to PII detection API endpoint
    try:
        response = requests.post(api_url, headers={'Content-Type': 'application/json'}, json={"text": data})
        response.raise_for_status()
        values = collect_unique_entities(response.json())
        return values
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to PII detection API ({api_url}): {e}")
        return None
    # print(data)