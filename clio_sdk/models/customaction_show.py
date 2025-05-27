
from pydantic import BaseModel

from .customaction import CustomactionOut


class CustomactionShowIn(BaseModel):
    data: CustomactionIn

class CustomactionShowOut(BaseModel):
    data: CustomactionOut

class CustomactionShowUpdate(BaseModel):
    data: CustomactionUpdate

class CustomactionShowDb(BaseModel):
    data: CustomactionDb

