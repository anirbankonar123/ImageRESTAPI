from pydantic import BaseModel
from typing import List

class Input(BaseModel):
    image:str

class Output(BaseModel):
    processedImage:str=""
    status:str="success"
    errorMsg:str=""

