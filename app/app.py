import core.predictor as predictor
import core.utils as utils
from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/xeye/*')


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/xeye/predict/url", methods=["POST"])
def predict_url():
    request_body = request.get_json()
    if request_body is None:
        return "Request body is empty."

    url = request_body["url"]
    if url is None:
        return "Url is empty."

    # Save image
    temp_image_file_save_path = utils.get_temp_path(app)

    # Predict
    try:
        utils.download(url, temp_image_file_save_path)
        prediction = predictor.predict(temp_image_file_save_path)
        utils.remove(temp_image_file_save_path)
    except Exception as e:
        utils.remove(temp_image_file_save_path)
        message = "Can't predict this url."
        print("# " + message)
        return {
            "status": "FAIL",
            "message": message
        }

    return {
        "status": "SUCCESS",
        "data": str(prediction)
    }


@app.route("/xeye/predict/file", methods=["POST"])
def predict():
    file = request.files['file']

    # Save image
    temp_image_file_save_path = utils.get_temp_file_path(app, file.filename)

    # Predict
    try:
        file.save(temp_image_file_save_path)
        prediction = predictor.predict(temp_image_file_save_path)
        utils.remove(temp_image_file_save_path)
    except Exception as e:
        utils.remove(temp_image_file_save_path)
        message = "Can't predict, file."
        print("# " + message)
        return {
            "status": "FAIL",
            "message": message
        }

    return {
        "status": "SUCCESS",
        "data": str(prediction)
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
