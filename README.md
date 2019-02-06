# Detecção de Emoções

A ideia é disponibilizarmos uma API de classificação de emoção com uma imagem dada de entrada e retornar um JSON das emoções detectadas. 


São 7 possíveis de emoções:

    NEUTRAL
    HAPPINES
    SADNESS
    ANGER
    FEAR
    SURPRISE
    DISGUST


## Install independencias with exception of Dlib
pip install -r requirements.txt

* Update requirements:
pip freeze > requirements.txt


## Install Dlib for Python

Tutorial: https://www.youtube.com/watch?v=h0Uidh-sq9M&t=43s

sudo apt-get update -y
sudo apt-get install build-essential cmake
sudo apt-get install libgtk-3-dev
sudo apt-get install libboost-all-dev
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo pip3 install numpy
sudo pip3 install scipy
sudo pip3 install scikit-image
sudo pip3 install dlib
sudo pip3 install face_recognition

Repositorio GitHub Dlib: https://github.com/davisking/dlib