# API Emotion Detection

The idea is to provide an emotion rating API with a given input image and return a JSON of the detected emotions.

There are 7 possible emotions:

    NEUTRAL
    HAPPINES
    SADNESS
    ANGER
    FEAR
    SURPRISE
    DISGUST

## Create virtual environment for the application

- pip install venv
- python3 -m venv venv
- . venv/bin/activate (ON environment)
- deactivate (OFF environment)

## Install lib of dependencies

Tutorial: https://www.youtube.com/watch?v=h0Uidh-sq9M&t=43s

- sudo apt-get update -y
- sudo apt-get install build-essential cmake
- sudo apt-get install libgtk-3-dev
- sudo apt-get install libboost-all-dev

Repositorio GitHub Dlib: https://github.com/davisking/dlib

## Install dependencies

pip install -r requirements.txt

- Update requirements:
  pip freeze > requirements.txt

## Up server API

- python api.py

## Use API

- Local file:
  Use requests GET in http://localhost:5000/api/inference
  JSON REQUESTS:

```json
{
  "ImageString": "[BASE64 DA IMAGEM]"
}
```

- JSON RESPONSE:

```json
{
  "BiggerEmotion": { "Emotion": "happiness", "Score": 0.9806605331437271 },
  "EmotionsDetects": [
    { "Emotion": "neutral", "Score": 0.01619137402179638 },
    { "Emotion": "happiness", "Score": 0.9806605331437271 },
    { "Emotion": "sadness", "Score": 7.412568437789737e-5 },
    { "Emotion": "anger", "Score": 5.644693053150985e-5 },
    { "Emotion": "fear", "Score": 0.0010004868147739541 },
    { "Emotion": "surprise", "Score": 0.0010941605854994415 },
    { "Emotion": "disgust", "Score": 0.0009228728192936613 }
  ]
}
```
