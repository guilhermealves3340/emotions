from flask_restful import Resource
from flask import request
from datetime import datetime
from hashlib import md5
import random as rd

from core.processor import detect_local, detect_upload


class Upload(Resource):

    def get(self):
        _file = request.files['file']
        _file.save('_temp/{}.jpg'.format(md5((str(datetime.now()) + str(rd.random())).encode()).hexdigest()))
        
        emotions = detect_upload(_file)
        return emotions
        

class Local(Resource):

    def get(self):      #TODO
        data = request.get_json(force=True)
        emotions = detect_local(data['path_file'])
        return emotions