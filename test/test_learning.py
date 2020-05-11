import os
import shutil

import core.predictor as predictor

IMAGE_HOME = "C:/Users/herme/Desktop/hyunkeun.park/workspace/ai/xeye/images"

# Compare image host
COMPARE_IMAGE_HOME = IMAGE_HOME + "/compare_web_image/2"
COMPARE_NORMAL_IMAGE_HOME = IMAGE_HOME + "/compare_normal_image"
COMPARE_PORN_IMAGE_HOME = IMAGE_HOME + "/compare_porn_image"

# Compare image
compare_image_list = os.listdir(COMPARE_IMAGE_HOME)
count = 0
for index in range(len(compare_image_list)):
    filename = compare_image_list[index]
    image_file_path = COMPARE_IMAGE_HOME + "/" + filename
    prediction = None
    try:
        print("Index: " + str(index) + ", image file: " + image_file_path)
        prediction = predictor.predict(image_file_path)
    except Exception as e:
        print("Can't predict, file: {}".format(image_file_path))
        continue

    count = count + 1
    # 0 : Porn image, 1 : Normal image
    if prediction[0].get("rate") > prediction[1].get("rate"):
        compare_image_file_path = COMPARE_PORN_IMAGE_HOME + "/" + filename
        shutil.copy(image_file_path, compare_image_file_path)
    else:
        compare_image_file_path = COMPARE_NORMAL_IMAGE_HOME + "/" + filename
        shutil.copy(image_file_path, compare_image_file_path)

print("Total: " + str(len(compare_image_list))
      + ", Predict: " + str(count)
      + ", Error: " + str(len(compare_image_list) - count))
