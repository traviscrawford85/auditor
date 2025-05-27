
from pydantic import BaseModel

from .myevent import MyeventOut


class MyeventShowIn(BaseModel):
    data: MyeventIn

class MyeventShowOut(BaseModel):
    data: MyeventOut

class MyeventShowUpdate(BaseModel):
    data: MyeventUpdate

class MyeventShowDb(BaseModel):
    data: MyeventDb

