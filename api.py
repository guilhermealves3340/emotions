from flask import Flask
from flask_restful import Resource, Api

from functions import Upload, Local


app = Flask(__name__)
api = Api(app)


api.add_resource(Local, '/api/local')
api.add_resource(Upload, '/api/upload')



if __name__ == '__main__':
    app.run(debug=True)