from flask import Flask, jsonify, request
from model import predictions
from io import BytesIO

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 8 * 1000 * 1000

@app.route("/", methods=['GET'])
def helloWorld():
    return jsonify({
        'status': 200,
        'message': "Hello, flask!!"
    })

@app.route("/medicalWaste", methods=['POST', 'GET'])
def getWastePrediction():
    if request.method == "GET":
        return jsonify({
            'status': 200,
            'message': "Endpoint called"
        })

    if request.method == "POST":
        file_upload = request.files['file']

        if file_upload:
            file_contents = file_upload.read()
            file_stream = BytesIO(file_contents)

            prediction_result = predictions(file_stream)
            prediction_result['probability'] = float(prediction_result['probability'])
            print(prediction_result)

            return jsonify({
                'status': 200,
                'message': "Success",
                'data': prediction_result
            })

        else:
            return jsonify({
                'status': 400,
                'message': "Upload a file"
            })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)