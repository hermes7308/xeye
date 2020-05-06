import os
import shutil
import uuid

import requests
from werkzeug.utils import secure_filename


def get_temp_path(app):
    return get_temp_file_path(app, str(uuid.uuid4()))


def get_temp_file_path(app, file_name):
    return os.path.join(app.root_path, 'temp', secure_filename(file_name))


def download(url, file_name):
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(file_name, 'wb') as file:
            request.raw.decode_content = True
            shutil.copyfileobj(request.raw, file)
