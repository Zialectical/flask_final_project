from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/emotionDetector", methods=["POST"])
def emotion_analyzer():
    text = request.form['textToAnalyze']
    response = emotion_detector(text)
    
    if response and 'dominant_emotion' in response:
        print(f"Passing emotions to template: {response}")  # Debugging print
        return render_template('result.html', emotions=response)
    else:
        return f"Error: Could not retrieve emotions. Full response: {response}"

if __name__ == "__main__":
    app.run(debug=True)