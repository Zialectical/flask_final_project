from flask import Flask, render_template, request
from emotion_detection import emotion_detector  # Import your emotion_detector function

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/emotionDetector", methods=["POST"])
def emotion_analyzer():
    text = request.form['textToAnalyze']
    emotions = emotion_detector(text)['emotion']['document']['emotion']
    
    # Pass emotions directly to the template without calculating the dominant emotion
    return render_template('result.html', emotions=emotions)

if __name__ == "__main__":
    app.run(debug=True)