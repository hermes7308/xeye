import csv
import os

import numpy as np
import tensorflow.keras
from PIL import Image, ImageOps

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model_file_path = ROOT_DIR + "\model\keras_model.h5"
print("Model file path: {}".format(model_file_path))
model = tensorflow.keras.models.load_model(model_file_path)

# Load the labels
labels = []
label_file_path = ROOT_DIR + "\model\labels.txt"
print("Label file path: {}".format(label_file_path))
with open(label_file_path, newline='') as csvfile:
    label_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in label_reader:
        labels.append(row[1] + "_" + row[2])
print("Labels: {}".format(labels))


def predict(image_file_path):
    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(image_file_path)

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

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)[0]

    result = {}
    for i in range(len(prediction)):
        result[i] = {
            "label": labels[i],
            "rate": prediction[i]
        }

    return result
