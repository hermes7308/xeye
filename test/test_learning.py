import os
import shutil

import core.predictor as predictor

IMAGE_HOME = "C:/Users/herme/Desktop/hyunkeun.park/workspace/ai/xeye/images"

# Original image home
NORMAL_IMAGE_HOME = IMAGE_HOME + "/normal_image"
# PORN_IMAGE_HOME = IMAGE_HOME + "/porn_image"
# PORN_IMAGE_HOME = IMAGE_HOME + "/redtube"
PORN_IMAGE_HOME = IMAGE_HOME + "/xxxvideo"

# Fail image home
FAIL_NORMAL_IMAGE_HOME = IMAGE_HOME + "/fail_normal_image"
FAIL_PORN_IMAGE_HOME = IMAGE_HOME + "/fail_porn_image"

# Compare image host
COMPARE_IMAGE_HOME = IMAGE_HOME + "/compare_web_image/11"
COMPARE_NORMAL_IMAGE_HOME = IMAGE_HOME + "/compare_normal_image"
COMPARE_PORN_IMAGE_HOME = IMAGE_HOME + "/compare_porn_image"

# Normal image
# normal_image_list = os.listdir(NORMAL_IMAGE_HOME)
# for index in range(len(normal_image_list)):
#     filename = normal_image_list[index]
#     image_file_path = NORMAL_IMAGE_HOME + "/" + filename
#     prediction = None
#     try:
#         print("Index: " + str(index) + ", image file: " + image_file_path)
#         prediction = predictor.predict(image_file_path)
#     except Exception as e:
#         print("Can't predict, file: {}".format(image_file_path))
#         continue
#     # 0 : Porn image, 1 : Normal image
#     if prediction[0].get("rate") > prediction[1].get("rate"):
#         fail_image_file_path = FAIL_NORMAL_IMAGE_HOME + "/" + filename
#         shutil.copy(image_file_path, fail_image_file_path)

# Porn image
# porn_image_list = os.listdir(PORN_IMAGE_HOME)
# for index in range(len(porn_image_list)):
#     filename = porn_image_list[index]
#     image_file_path = PORN_IMAGE_HOME + "/" + filename
#     prediction = None
#     try:
#         print("Index: " + str(index) + ", image file: " + image_file_path)
#         prediction = predictor.predict(image_file_path)
#     except Exception as e:
#         print("Can't predict, file: {}".format(image_file_path))
#         continue
#     # 0 : Porn image, 1 : Normal image
#     if prediction[0].get("rate") < prediction[1].get("rate"):
#         fail_image_file_path = FAIL_PORN_IMAGE_HOME + "/" + filename
#         shutil.copy(image_file_path, fail_image_file_path)


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

print("Total: " + str(len(compare_image_list)) + ", Predict: " + str(count))
