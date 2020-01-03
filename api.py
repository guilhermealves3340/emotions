from flask import Flask, request, jsonify
from flask_cors import CORS
import execute
from payloadSchemas import *

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/face-recognition', methods=['GET'])
def inference():
    data = request.get_json(force=True)
    payload, err = check(data, inferenceSchema)
    if err:
        return jsonify({'error': err}), 400
    return jsonify(execute.runInference(payload)), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
