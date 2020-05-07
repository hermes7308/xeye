import core.predictor as predictor

# Predict normal image
normal_image_prediction = predictor.predict("C:/Users/herme/Desktop/hyunkeun.park/workspace/ai/xeye/images/xxxvideo/1.jpg")
print("Image 01: {}".format(normal_image_prediction))

# Predict normal image
porn_image_prediction = predictor.predict("../data/porn_image01.jpg")
print("Image 02: {}".format(porn_image_prediction))