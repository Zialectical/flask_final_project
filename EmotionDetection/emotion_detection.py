import requests
import json
from requests.auth import HTTPBasicAuth

def emotion_detector(text_to_analyze):
    # Check for blank input
    if not text_to_analyze.strip():
        # Return None for all emotions if the input is blank
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    api_key = "xDE5qRNoiHskqBOZhBjwjoYUFfiaj5XMhRqWvZDWoX-U"
    url = "https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/b3c74d73-d01f-4436-9e71-779b0c072a36/v1/analyze?version=2021-08-01"
    
    headers = {"Content-Type": "application/json"}
    payload = {
        "text": text_to_analyze,
        "features": {"emotion": {}}
    }

    try:
        response = requests.post(url, headers=headers, json=payload, auth=HTTPBasicAuth("apikey", api_key))

        # Handle status_code = 400
        if response.status_code == 400:
            # Return None for all emotions
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        response_data = response.json()

        # Extract emotion scores
        emotions = response_data['emotion']['document']['emotion']
        anger = emotions.get('anger', 0)
        disgust = emotions.get('disgust', 0)
        fear = emotions.get('fear', 0)
        joy = emotions.get('joy', 0)
        sadness = emotions.get('sadness', 0)

        # Find the dominant emotion
        emotions_dict = {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness}
        dominant_emotion = max(emotions_dict, key=emotions_dict.get)

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