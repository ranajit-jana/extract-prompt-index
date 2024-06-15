import requests
import json

def make_api_call(data, llm_server_url):
    jsondata = {"text": data, "key2": "value2"}
    response = requests.post(llm_server_url, json=jsondata)
    if response.status_code == 200:
        response_text_data = json.loads(response.text)
        return response_text_data
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    import sys
    data = sys.argv[1]
    llm_server_url = sys.argv[2]
    response = make_api_call(data, llm_server_url)
    print(response)
