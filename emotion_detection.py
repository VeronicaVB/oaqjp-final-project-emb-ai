import requests  # Import the requests library to handle HTTP requests


def emotion_detector(text_to_analyse):
    url = 'http://localhost:8080/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment
    # analysis service
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers
    myobj = {"raw_document": {"text": text_to_analyse}}  # Create a dictionary with the
    # text to be analyzed
    response = requests.post(url, json=myobj, headers=headers)

    return response.text


