import cv2

from core.faces import FaceDetector
from core.data import FaceData
from core.gabor import GaborBank
from core.emotions import EmotionsDetector


class FrameData:

    def __init__(self):
        self._faceDet = FaceDetector()
        self._bank = GaborBank()
        self._emotionsDet = EmotionsDetector()
        self._face = FaceData()
        self._emotions = {}
    
    def detect(self, frame):
        ret, face = self._faceDet.detect(frame)
        if ret:
            frame, face = face.crop(frame)
            responses = self._bank.filter(frame)
            self._emotions = self._emotionsDet.detect(face, responses)
            return True
        else:
            self._face = None
            return False

def detect_emotions(_file):
    frame = cv2.imread(_file)
    data = FrameData()
    face = data.detect(frame)
    if face != None:
        return {
            'emotions': dict(data._emotions),
            'src': _file,
            'bigger_emotion': {
                'emotion': list(data._emotions.keys())[list(data._emotions.values()).index(max(list(data._emotions.values())))],
                'score': max(list(data._emotions.values()))
            }
        }
    else:
        return {'error': 'face not found'}