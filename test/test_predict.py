import core.predictor as predictor

# Predict normal image
normal_image_prediction = predictor.predict("C:/Users/herme/Desktop/hyunkeun.park/workspace/ai/xeye/images/grayscale_porn_image_200/6.jpg")
print("Image 01: {}".format(normal_image_prediction))

# Predict normal image
porn_image_prediction = predictor.predict("../static/image/porn_image01.jpg")
print("Image 02: {}".format(porn_image_prediction))