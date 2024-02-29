from fastapi import FastAPI, File, UploadFile,Response
from starlette.responses import FileResponse

import uvicorn

from app import data_models
from utils import image_utils
import base64
from typing import Union

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Hello World"}

"""
This POST API accepts an image in the Base64 encoded format, and returns the modified image
"""
@app.post("/process/encodedimage",response_model=data_models.Output)
async def image_api(input:data_models.Input,input_format: Union[str, None] = None):

    if (input_format==None):
        input_format="png"
    print("input_format:" + input_format)

    if ((not (input_format == "png")) & (not (input_format == "jpg"))):                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        output = data_models.Output()
        output.status = "failure"
        output.errorMsg = "Input format can be jpg and png only "
        output.itemCount = 0
        return output

    #Convert base64 string to Image and write to temp image file
    try:
        image_utils.base64str_to_PILImage(input.image,input_format)
    except BaseException as err:
        output = data_models.Output()
        output.status = "failure"
        output.errorMsg = "Error in decoding Base64 string"
        output.itemCount = 0
        return output

    #Do pre-processing on the image (grayscaling, hist eq, resizing and write pre-processed temp image file)
    file_nm = image_utils.write_preprocessed_img(input_format,input)

    with open(file_nm, "rb") as image_file:
        base64str = base64.b64encode(image_file.read()).decode("utf-8")

    output = data_models.Output()
    output.processedImage = base64str

    return output


if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=False, root_path="/")
