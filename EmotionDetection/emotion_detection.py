import requests
import json

def emotion_detector(text_to_analyse):
    """
    Exécute l'analyse d'émotion et gère les entrées vides
    via le code de statut HTTP.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Exécution de l'application (même avec une entrée vide)
    response = requests.post(url, json=myobj, headers=header)
    
    # Accès à l'attribut status_code
    status_code = response.status_code
    
    # Gestion de l'entrée vide (code 400)
    if status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    # Traitement normal (code 200)
    elif status_code == 200:
        formated_response = json.loads(response.text)
        emotions = formated_response['emotionPredictions'][0]['emotion']
        
        dominant_emotion = max(emotions, key=emotions.get)
        
        return {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }