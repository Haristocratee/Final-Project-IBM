"""
Serveur Flask pour le déploiement de l'application de détection d'émotions.
Ce module définit les routes pour l'interface web et l'API d'analyse.
"""

from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """
    Gère la route principale ('/').
    Rend et affiche la page web index.html à l'utilisateur.
    """
    return render_template('index.html')


@app.route("/emotionDetector")
def emo_detector():
    """
    Gère la route /emotionDetector.
    Récupère le texte de la requête utilisateur, l'analyse via
    la fonction emotion_detector et retourne le résultat formaté.
    Gère également les entrées vides.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Texte invalide ! Veuillez réessayer !"

    formatted_response = (
        f"Pour l'énoncé donné, la réponse du système est "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} et "
        f"'sadness': {response['sadness']}. "
        f"L'émotion dominante est {response['dominant_emotion']}."
    )

    return formatted_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)