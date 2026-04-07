import requests
import json

def emotion_predictor(text_to_analyse):
    # API configuration and payload setup
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    
    # Executing the request and capturing the .text attribute
    response = requests.post(url, json=input_json, headers=headers)
    response_text = response.text
    
    # Converting the string response into a dictionary
    response_dict = json.loads(response_text)
    
    # Extracting the emotion scores from the nested structure
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    # Mapping individual scores to variables
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Logic to identify the dominant emotion (key with the maximum value)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Formatting the output as requested
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

# Example of how to call the function:
# print(emotion_predictor("I am incredibly happy with these results!"))