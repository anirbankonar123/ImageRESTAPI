import base64
from PIL import Image
import io
import argparse

base64str = ""


def base64str_to_PILImage(base64str):
   base64_img_bytes = base64str.encode('utf-8')
   base64bytes = base64.b64decode(base64_img_bytes)
   bytesObj = io.BytesIO(base64bytes)
   img = Image.open(bytesObj)
   img.save("tmp1.jpg")
   return img


base64str_to_PILImage(base64str)