from flask_restful import Resource, reqparse
from flask import request
import werkzeug

from core.processor import Recognition

from datetime import datetime
from hashlib import md5
import random as rd
import os

class Upload(Resource):

    def post(self):
        f = request.files['file']
        f.save('_temp/{}.jpg'.format(md5((str(datetime.now()) + str(rd.random())).encode()).hexdigest()))
        return {
            'status': 'sucess',
            'path_file': path_file
        }
        

class Local(Resource):

    def get(self):      #TODO
        data = request.get_json(force=True)
        processor = Recognition(data['path_file'])
        emotions = processor.detect_local()
        return emotions