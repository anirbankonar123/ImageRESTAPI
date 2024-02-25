import base64
from PIL import Image
import io
import argparse

base64str = ""

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=False,help="path to input image to be encoded")
args = vars(ap.parse_args())

if (args["image"]):
    image_path=args["image"]

with open(image_path,"rb") as image_file:
    base64str = base64.b64encode(image_file.read()).decode("utf-8")

file_obj = open("tmp.txt", "w")
file_obj.write(base64str)
file_obj.close()

