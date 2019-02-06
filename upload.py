from flask_restful import Resource, reqparse
import werkzeug

from core.main import recognition


class Upload(Resource):

    def get(self):

        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()
        recognition(args['file'])               
        
        return {
            'status': 'sucess'
        }