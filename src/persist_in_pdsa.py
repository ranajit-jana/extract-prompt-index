import requests
import json

def persist_in_pdsa(api_url, data):
    # Function to persist data in Persistent Storage and Data Analysis (PDSA) API

    try:
        json_data = json.dumps(data).encode('utf8')
        # print(f"Sending data: \n {data}")
        response = requests.post(api_url, json_data, headers={"Content-Type": "application/json"})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error persisting data to PDSA API ({api_url}): {e}")
        return None
