from flask_restful import Resource, reqparse

from core.main import recognition


class Local(Resource):

    def get(self):

        return {
            'status': 'sucess'
        }