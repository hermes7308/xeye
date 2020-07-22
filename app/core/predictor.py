import csv
import os

import numpy as np
import tensorflow.keras
from PIL import Image, ImageOps

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the labels
labels = []
label_file_path = os.path.join(ROOT_DIR, "model", "labels.txt")
with open(label_file_path, newline='') as csvfile:
    label_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in label_reader:
        labels.append(row[1] + "_" + row[2])
print("# Label file path: {}".format(label_file_path))
print("# Labels: {}".format(labels))

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model_file_path = os.path.join(ROOT_DIR, "model", "keras_model.h5")
model = tensorflow.keras.models.load_model(model_file_path)
print("# Model file path: {}".format(model_file_path))


def predict(image_file_path):
    # Replace this with the path to your image
    image = Image.open(image_file_path)

    # L: gray-scale, RGB: color
    if image.mode is not 'RGB':
        image = image.convert(mode="RGB")

    # resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # display the resized image
    # image.show()

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)[0]

    return {
        labels[0]: round(prediction[0], 3),  # PORN_IMAGE
        labels[1]: round(prediction[1], 3),  # NORMAL_IMAGE
    }
