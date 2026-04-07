"""
This module provides the main server logic for the application.
It handles incoming requests and manages database connections.
"""
from flask import Flask, render_template, request
from emotion_detection import emotion_predictor

app = Flask("Emotion Detector")

'''
This function loads the emotionDetector path.
'''
@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_predictor(text_to_analyze)

    # Extract the dominant emotion
    dominant_emotion = response['dominant_emotion']

    # If the function returned None (due to status_code 400), display error message
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Otherwise, return the formatted successful response
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is "
        f"**{dominant_emotion}**."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main application page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Deploy the application on localhost:5000
    app.run(host="0.0.0.0", port=5000)
