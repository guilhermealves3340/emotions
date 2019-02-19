from flask_restful import Resource
from flask import request
from datetime import datetime
from hashlib import md5
import random as rd

from core.engine import processor


class Upload(Resource):

    def get(self):
        try:
            _file = request.files['file']
            _file_name = '_temp/{}.jpg'.format(md5((str(datetime.now()) + str(rd.random())).encode()).hexdigest())
            _file.save(_file_name)  
            return detect_emotions(_file_name)
        except:
            return 'File invalid'
        

class Local(Resource):

    def get(self):
        try:
            data = request.get_json(force=True)
            return processor(data['path_file'])
        except:
            return 'File invalid'