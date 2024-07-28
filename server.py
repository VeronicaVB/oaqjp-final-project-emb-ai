"""
Server for the Emotion Detector final project
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/emotionDetector')
def emo_detector():
    """
    This code gets the text from the html interface and runs the emotion detector.
    :return: String
    """
    text_to_analise = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analise)

    if response['dominant_emotion'] != 'None':
        dominant_emotion = response[
            'dominant_emotion']
    else:
        dominant_emotion = 'Invalid text! Please try again!'

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    return (
        f"For the given statement, the system response is anger:{anger}, disgust: {disgust}, "
        f"fear{fear}, joy:{joy}, and"
        f"sadness: {sadness}. The dominant emotion is: {dominant_emotion}")


@app.route("/")
def render_index_page():
    """ This function initiates the rendering of the main application
        page over the Flask channel
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
