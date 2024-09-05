from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/emotionDetector", methods=["POST"])
def emotion_analyzer():
    text = request.json.get('textToAnalyze')  # Fetch from JSON body
    response = emotion_detector(text)
    
    if response and 'dominant_emotion' in response:
        # Format the response as required
        formatted_response = (
            f"For the given statement, the system response is 'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}, "
            f"and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
        )
        return jsonify({"result": formatted_response})
    else:
        return jsonify({"error": "Could not retrieve emotions."}), 400

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)