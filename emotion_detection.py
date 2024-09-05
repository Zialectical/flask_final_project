import requests
import json
from requests.auth import HTTPBasicAuth

def emotion_detector(text_to_analyze):
    api_key = "xDE5qRNoiHskqBOZhBjwjoYUFfiaj5XMhRqWvZDWoX-U"
    url = "https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/b3c74d73-d01f-4436-9e71-779b0c072a36/v1/analyze?version=2021-08-01"
    
    headers = {"Content-Type": "application/json"}
    
    payload = {
        "text": text_to_analyze,
        "features": {"emotion": {}}
    }

    try:
        print("Sending request to Watson API...")  # Debugging print
        response = requests.post(url, headers=headers, json=payload, auth=HTTPBasicAuth("apikey", api_key))
        response_data = response.json()

        # Print the full Watson API response to understand the structure
        print("Full Watson API response: ", json.dumps(response_data, indent=4))

        # Extract emotion scores from the proper location in the response
        emotions = response_data['emotion']['document']['emotion']
        anger = emotions.get('anger', 0)
        disgust = emotions.get('disgust', 0)
        fear = emotions.get('fear', 0)
        joy = emotions.get('joy', 0)
        sadness = emotions.get('sadness', 0)

        # Debugging print to see if these values are correct
        print(f"Extracted values - Anger: {anger}, Disgust: {disgust}, Fear: {fear}, Joy: {joy}, Sadness: {sadness}")
        
        emotions_dict = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }
        dominant_emotion = max(emotions_dict, key=emotions_dict.get)
        
        print(f"Dominant emotion: {dominant_emotion}")  # Debugging dominant emotion

        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

# Test the function
if __name__ == "__main__":
    result = emotion_detector("I am so happy I am doing this.")
    print(result)  # Debugging print