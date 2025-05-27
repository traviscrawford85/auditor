from typing import List

from pydantic import BaseModel

from .myevent import MyeventOut


class MyeventListIn(BaseModel):
    data: List[MyeventIn]

class MyeventListOut(BaseModel):
    data: List[MyeventOut]

class MyeventListUpdate(BaseModel):
    data: List[MyeventUpdate]

class MyeventListDb(BaseModel):
    data: List[MyeventDb]

