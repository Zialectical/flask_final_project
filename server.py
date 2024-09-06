"""
This module contains the Flask server for emotion detection.
It defines routes for the application and handles emotion analysis requests.
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Render the index page where users can input text for analysis.

    Returns:
        Rendered HTML template for the index page.
    """
    return render_template('index.html')

@app.route("/emotionDetector", methods=["POST"])
def emotion_analyzer():
    """
    Analyze the emotions from the input text using the Watson API.

    Returns:
        Rendered result.html template with the emotions or an error message.
    """
    text = request.form['textToAnalyze']
    response = emotion_detector(text)

    if response and response['dominant_emotion'] is not None:
        # Pass the emotions to the template
        return render_template('result.html', emotions=response)
    else:
        # Handle blank input or API error
        return render_template('result.html', emotions={
            'anger': 'N/A', 
            'disgust': 'N/A', 
            'fear': 'N/A', 
            'joy': 'N/A', 
            'sadness': 'N/A', 
            'dominant_emotion': 'Invalid text! Please try again.'
        })

if __name__ == "__main__":
    app.run(debug=True)
