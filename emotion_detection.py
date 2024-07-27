import requests  # Import the requests library to handle HTTP requests
import json


def emotion_detector(text_to_analyse):
    url = 'http://localhost:8080/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment
    # analysis service
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers
    myobj = {"raw_document": {"text": text_to_analyse}}  # Create a dictionary with the
    # text to be analyzed
    response = requests.post(url, json=myobj, headers=headers)

    formatted_response = json.loads(response.text)
    emotions = (formatted_response['emotionPredictions'][0])

    anger_score = emotions['emotion']['anger']
    disgust_score = emotions['emotion']['disgust']
    fear_score = emotions['emotion']['fear']
    joy_score = emotions['emotion']['joy']
    sadness_score = emotions['emotion']['sadness']
    dominant_emotion = max([anger_score, disgust_score, fear_score, joy_score, sadness_score])

    output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    return output
