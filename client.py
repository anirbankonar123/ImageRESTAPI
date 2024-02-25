import requests
import base64
import argparse
import time
from PIL import Image
import io

base64str = ""

URL = "http://127.0.0.1:8000/process/encodedimage?input_format=jpg"
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="path to input image to be processed")
ap.add_argument("-o", "--output", required=False,help="Filename to store results")

args = vars(ap.parse_args())



if ((not (args["image"])) ):
    print("image is mandatory")
print(URL)

def base64str_to_PILImage(base64str,image_path):
   base64_img_bytes = base64str.encode('utf-8')
   base64bytes = base64.b64decode(base64_img_bytes)
   bytesObj = io.BytesIO(base64bytes)
   img = Image.open(bytesObj)
   img.save(image_path)
   return img


if (args["image"]):
    image_path=args["image"]

    print(image_path)
    with open(image_path,"rb") as image_file:
        base64str = base64.b64encode(image_file.read()).decode("utf-8")

    image_json = {
        "image": base64str
    }

    start = time.perf_counter()

    response = requests.post(url=URL,json=image_json)
    request_time = time.perf_counter() - start
    print("Request completed in {0:.0f}ms".format(request_time))
    print("RESPONSE JSON")
    #print(response.json())

    encoded_Image = response.json()["processedImage"]

    if (args["output"]):
        output_path = args["output"]
    else:
        output_path = "output.jpg"
    base64str_to_PILImage(base64str,output_path)

