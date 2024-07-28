from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/emotionDetector')
def emo_detector():
    '''
    This code gets the text from the html interface and runs the emotion detector.
    :return: String
    '''
    text_to_analise = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analise)

    dominant_emotion = 'Invalid text! Please try again!' if response['dominant_emotion'] == 'None' else response['dominant_emotion']

    return ("For the given statement, the system response is anger: {}, "
            "disgust:{}, fear:{}, joy:{} and sadness:{}. The dominant emotion is:{}.").format(response['anger'],
                                                                                              response['disgust'],
                                                                                              response['fear'],
                                                                                              response['joy'],
                                                                                              response['sadness'],
                                                                                              dominant_emotion)
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(debug=True)
