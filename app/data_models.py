from pydantic import BaseModel
from typing import List

class FilterParam(BaseModel):
    paramKey:str=""
    paramValue:str=""

class ImageFilter(BaseModel):
    filterName:str=""
    filterParams:List[FilterParam] = []

class Input(BaseModel):
    image:str
    filters: List[ImageFilter] = []

class Output(BaseModel):
    processedImage:str=""
    status:str="success"
    errorMsg:str=""

