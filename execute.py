import base64
from PIL import Image
import numpy as np
import io

from core.engine import processor


def runInference(payload):
    imgByte = base64.b64decode(payload['ImageString'])
    imgPIL = Image.open(io.BytesIO(imgByte))
    data = processor(np.asarray(imgPIL))
    if not data:
        return {'error': 'face not found'}

    def getBiggerEmotion(data):
        maxScore = max(list(data.emotions.values()))
        return {
            'Score': maxScore,
            'Emotion': list(data.emotions.keys())[list(data.emotions.values()).index(maxScore)]
        }

    def getEmotions(data):
        emotions = []
        for emotion in data.emotions.keys():
            emotions.append(
                {'Score': data.emotions[emotion], 'Emotion': emotion})
        return emotions

    result = {
        'BiggerEmotion': getBiggerEmotion(data),
        'EmotionsDetects': getEmotions(data)
    }
    return result
