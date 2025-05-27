from typing import List

from pydantic import BaseModel

from .customfield import CustomfieldOut


class CustomfieldListIn(BaseModel):
    data: List[CustomfieldIn]

class CustomfieldListOut(BaseModel):
    data: List[CustomfieldOut]

class CustomfieldListUpdate(BaseModel):
    data: List[CustomfieldUpdate]

class CustomfieldListDb(BaseModel):
    data: List[CustomfieldDb]

