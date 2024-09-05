import requests
import json
from requests.auth import HTTPBasicAuth  # Use this for Basic Authentication

def emotion_detector(text_to_analyze):
    # Watson API key and correct endpoint for NLU analyze action
    api_key = "xDE5qRNoiHskqBOZhBjwjoYUFfiaj5XMhRqWvZDWoX-U"
    url = "https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/b3c74d73-d01f-4436-9e71-779b0c072a36/v1/analyze?version=2021-08-01"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    # Payload for NLU emotion analysis
    payload = {
        "text": text_to_analyze,
        "features": {
            "emotion": {}
        }
    }

    try:
        print("Sending request to Watson API...")  # Debugging print
        # Using HTTPBasicAuth for Basic Authentication with API key
        response = requests.post(url, headers=headers, json=payload, auth=HTTPBasicAuth("apikey", api_key))
        
        # Print the raw response from the API before raising for status
        print("Raw response:", response.text)
        
        response.raise_for_status()  # Checks for HTTP errors
        print("Response received.")  # Debugging print
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")  # Print the error if any occurs
        return None

# Testing the function by calling it in the main block
if __name__ == "__main__":
    print("Starting emotion detection test")  # Check if the function starts
    result = emotion_detector("I love this new technology.")
    print("Test completed, result:", result)  # Print the final result