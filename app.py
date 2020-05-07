import os

from flask import Flask, render_template, request

import core.predictor as predictor
import core.utils as utils

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/test/xeye/predict/upload", methods=["GET"])
def xeye_predict_upload_page():
    return render_template("xeye_predict_upload_page.html")


@app.route("/xeye/predict/file", methods=["POST"])
def predict():
    f = request.files['file']

    # Save image
    temp_image_file_save_path = utils.get_temp_file_path(app, f.filename)
    f.save(temp_image_file_save_path)

    # Predict
    try:
        prediction = predictor.predict(temp_image_file_save_path)
        os.remove(temp_image_file_save_path)
    except Exception as e:
        os.remove(temp_image_file_save_path)
        message = "Can't predict, file."
        print(message)
        return {
            "status": "FAIL",
            "message": message
        }

    # Remove

    return {
        "status": "SUCCESS",
        "data": str(prediction)
    }


@app.route("/xeye/predict/url", methods=["POST"])
def predict_url():
    request_body = request.get_json()
    url = request_body["url"]
    if url is None:
        return "Url is empty."

    # Save image
    temp_image_file_save_path = utils.get_temp_path(app)
    utils.download(url, temp_image_file_save_path)

    # Predict
    try:
        prediction = predictor.predict(temp_image_file_save_path)
        os.remove(temp_image_file_save_path)
    except Exception as e:
        os.remove(temp_image_file_save_path)
        message = "Can't predict image file."
        print(message)
        return {
            "status": "FAIL",
            "message": message
        }

    return {
        "status": "SUCCESS",
        "data": str(prediction)
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
