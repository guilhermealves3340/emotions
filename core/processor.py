"""
    NEUTRAL
    HAPPINES
    SADNESS
    ANGER
    FEAR
    SURPRISE
    DISGUST 
"""

import sys
import argparse
import cv2
from collections import OrderedDict
import pprint as p

from core.faces import FaceDetector
from core.data import FaceData
from core.gabor import GaborBank
from core.emotions import EmotionsDetector


class FrameData:
    """
    Helper class to present the detected face region, landmarks and emotions.
    """
    #-----------------------------------------
    def __init__(self):
        """
        Classe construtor.
        """

        self._faceDet = FaceDetector()
        '''
        A instância do detector de face.
        '''

        self._bank = GaborBank()
        '''
        A instância do banco de filtros Gabor.
        '''

        self._emotionsDet = EmotionsDetector()
        '''
        A instância do detector de emoções.
        '''

        self._face = FaceData()
        '''
        Dados da última face detectada.
        '''

        self._emotions = {}
        '''
        Dados das últimas emoções detectadas.
        '''
    
    def detect(self, frame):
        """
        Detecta uma face e as emoções prototípicas na imagem do frame.

        """
        ret, face = self._faceDet.detect(frame)
        if ret:
            self._face = face

            # Cortar apenas a região da face
            frame, face = face.crop(frame)

            # Filtrar com o banco Gabor
            responses = self._bank.filter(frame)

            # Detectar as emoções prototípicas com base nas respostas do filtro
            self._emotions = self._emotionsDet.detect(face, responses)

            return True
        else:
            self._face = None
            return False

    
    def draw(self, frame):
        """
        Desenha os dados detectados da imagem do frame fornecida.

        """
        empty = True

         # Traçar os marcos da face e distância do rosto
        x = 5
        y = 0
        w = int(frame.shape[1]* 0.2)
        try:
            face = self._face
            empty = face.isEmpty()
            face.draw(frame)
        except:
            pass 

        # Plot the emotion probabilities
        try:
            emotions = self._emotions
            if empty:
                labels = []
                values = []
            else:
                labels = list(emotions.keys())                                  ## Lista com as emoções disponíveis
                values = list(emotions.values())                                ## Lista com 
                bigger = labels[values.index(max(values))]                      ## MAIOR PROBABILIDADE

                print(bigger)                                                   ## PRINTANDO A EMOÇÃO COM MAIOR PROBABILIDADE

        except Exception as e:
            print(e)
            pass

class Recognition:

    def __init__(self, _file):
        self._file = _file
        self.data = FrameData()


    def detect_local(self):
        frame = cv2.imread(self._file)
        data = FrameData()
        data.detect(frame)
        result = dict(data._emotions)
        result['src'] = self._file
        result['bigger_emotion'] = {
            'emotion': list(self.emotions.keys()).index(max(list(self._emotions.values()))),
            'score': max(list(self._emotions.values()))
        }
        return result


    def detect_upload(self):
        pass


def testes(path):
    '''ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
        help="path to input image")
    args = vars(ap.parse_args())'''

    photo = cv2.imread(path)
    data = FrameData()
    #frame = photo.copy()
    data.detect(photo)
    p.pprint(data._emotions)
    return data._emotions
    #data.draw(frame)
