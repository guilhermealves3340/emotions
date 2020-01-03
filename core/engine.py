import cv2

from core.faces import FaceDetector
from core.data import FaceData
from core.gabor import GaborBank
from core.emotions import EmotionsDetector


class FrameData:

    def __init__(self):
        self.faceDet = FaceDetector()
        self.bank = GaborBank()
        self.emotionsDet = EmotionsDetector()
        self.face = FaceData()
        self.emotions = {}

    def detect(self, frame):
        ret, face = self.faceDet.detect(frame)
        if ret:
            frame, face = face.crop(frame)
            responses = self.bank.filter(frame)
            self.emotions = self.emotionsDet.detect(face, responses)
            return True
        else:
            self.face = None
            return False


def processor(frame):
    data = FrameData()
    face = data.detect(frame)
    if face:
        return data

    else:
        return None
