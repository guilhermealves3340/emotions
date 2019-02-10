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

* pip install venv
* python3 -m venv venv
* . venv/bin/activate (ON environment)
* deactivate (OFF environment)


## Install lib of dependencies

Tutorial: https://www.youtube.com/watch?v=h0Uidh-sq9M&t=43s

* sudo apt-get update -y
* sudo apt-get install build-essential cmake
* sudo apt-get install libgtk-3-dev
* sudo apt-get install libboost-all-dev

Repositorio GitHub Dlib: https://github.com/davisking/dlib


## Install dependencies

pip install -r requirements.txt

* Update requirements:
pip freeze > requirements.txt


## Up server API

* python api.py


## Use API

* Local file:
Use requests GET in http://localhost:5000/api/local
JSON REQUESTS: 
```json
{
    "path_file": "[PATH OF FILE IN FOULDER]" 
}

```

* Upload file:
Use requests GET in http://localhost:5000/api/upload
Send file with key = 'file'

* JSON RESPONSE: 

```json
{
    "emotions": {
        "neutral": 0.09924766274118275,
        "happiness": 0.19784566900071152,
        "sadness": 0.00850921345255757,
        "anger": 0.02736034770887536,
        "fear": 0.02820437791581977,
        "surprise": 0.6305306379481774,
        "disgust": 0.008302091232675795
    },
    "src": "/home/guilherme/Imagens/p000001782.jpg",
    "bigger_emotion": {
        "emotion": "surprise",
        "score": 0.6305306379481774
    }
}

```
