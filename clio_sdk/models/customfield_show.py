
from pydantic import BaseModel

from .customfield import CustomfieldOut


class CustomfieldShowIn(BaseModel):
    data: CustomfieldIn

class CustomfieldShowOut(BaseModel):
    data: CustomfieldOut

class CustomfieldShowUpdate(BaseModel):
    data: CustomfieldUpdate

class CustomfieldShowDb(BaseModel):
    data: CustomfieldDb

