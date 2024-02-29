from PIL import Image, ImageOps, ImageEnhance
import cv2
import numpy as np
import base64
import io

# import detectron2
# from detectron2.utils.logger import setup_logger
# setup_logger()
#logging.getLogger('detectron2').setLevel(logging.WARNING)

# import some common libraries
import numpy as np
import os, json, cv2, random
import copy
import matplotlib.pyplot as plt
import imutils



# import some common detectron2 utilities
# from detectron2 import model_zoo
# from detectron2.engine import DefaultPredictor
# from detectron2.engine import DefaultTrainer
# from detectron2.config import get_cfg
# from detectron2.data import detection_utils as utils
# import detectron2.data.transforms as T
# from detectron2.utils.visualizer import Visualizer
# from detectron2.data import MetadataCatalog, DatasetCatalog,build_detection_test_loader, build_detection_train_loader
#
# from detectron2.data.datasets import register_coco_instances
# from detectron2.utils.visualizer import ColorMode
#
#
# def predict(img):
#     try:
#         DatasetCatalog.remove("coco_train")
#         DatasetCatalog.clear()
#         MetadataCatalog.clear()
#     except BaseException:
#         pass
#     finally:
#         register_coco_instances(f"coco_train", {}, f"<coco json file",
#                                 f"<image folder>/")
#         MetadataCatalog.get("coco_train").set(thing_classes=["<defect class>"])
#         dataset_dicts = DatasetCatalog.get("coco_train")
#         coco_metadata = MetadataCatalog.get("coco_train")
#
#     cfg = get_cfg()
#     cfg.MODEL.DEVICE = 'cpu'
#     cfg.merge_from_file(model_zoo.get_config_file('COCO-InstanceSegmentation/mask_rcnn_R_101_FPN_3x.yaml'))
#     cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
#     cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1
#     cfg.MODEL.WEIGHTS = os.path.join("output", "model_final.pth")
#
#     predictor = DefaultPredictor(cfg)
#
#     outputs = predictor(img)
#     print("number of instances")
#     print(str(len(outputs["instances"])))
#     v = Visualizer(img[:, :, ::-1],
#                    metadata=coco_metadata,
#                    scale=0.5,
#                    instance_mode=ColorMode.SEGMENTATION
#                    )
#     out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
#     cv2.imwrite("output.jpg",out.get_image()[:, :, ::-1])
#     return "output.jpg"


"""
This method converts the base64 encoded string into Image object and saves this to temporary location 
"""
def base64str_to_PILImage(base64str,input_format):
   base64_img_bytes = base64str.encode('utf-8')
   base64bytes = base64.b64decode(base64_img_bytes)
   bytesObj = io.BytesIO(base64bytes)
   img = Image.open(bytesObj)
   if (input_format=="png"):
       img.save("tmp.png")
   elif ((input_format=="jpg")):
       img.save("tmp.jpg")
   return img

"""
This method resizes the image, based on image width and ht, and target width and ht. If the img size is smaller
than target , it zero pads the image, if the size is larger than target it fits the image with LANCZOS filtering
"""
def resize_image(img,w,h,img_width,img_height):
    if (h<img_height):
        #print("padding")
        delta_width = img_width - w
        delta_height = img_height - h
        pad_width = delta_width // 2
        pad_height = delta_height // 2
        padding = (pad_width, pad_height, delta_width - pad_width, delta_height - pad_height)
        resized_img = ImageOps.expand(img, padding)
    else:
        #print("fitting")
        resized_img = ImageOps.fit(img,(img_width,img_height),method=Image.LANCZOS) #,method=Image.LANCZOS
    return resized_img

"""
This method reads the temporary image and applies the filters passed in Input object
and writes the pre-processed image
"""
def write_preprocessed_img(input_format,input):

    if (input_format=="png"):
        img = cv2.imread("tmp.png")
    elif (input_format=="jpg"):
        img = cv2.imread("tmp.jpg")
    (h, w, c) = img.shape[:3]

    print("applying adaptive hist eq")
    clahe = cv2.createCLAHE(clipLimit=5)
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image = clahe.apply(image)

    if (input_format == "png"):
        file_nm = "tmp.png"
    elif (input_format == "jpg"):
        file_nm = "tmp.jpg"

    cv2.imwrite(file_nm, image)

    return file_nm


