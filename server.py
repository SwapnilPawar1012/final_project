"""
server.py
"""
from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """
    function for initial reader of index.html page.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def sent_emotion_detector():
    """
    function for emotion detector.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        return jsonify({"message": "Invalid text! Please try again!"})

    return f"""For the give statement, the system response is 'anger': {anger}, 
'disgust':{disgust}, 'fear':{fear}, 'joy':{joy} and 'sadness':{sadness}. 
The dominant emotion is <b>{dominant_emotion}</b>."""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
