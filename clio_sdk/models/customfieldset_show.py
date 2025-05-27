
from pydantic import BaseModel

from .customfieldset import CustomfieldsetOut


class CustomfieldsetShowIn(BaseModel):
    data: CustomfieldsetIn

class CustomfieldsetShowOut(BaseModel):
    data: CustomfieldsetOut

class CustomfieldsetShowUpdate(BaseModel):
    data: CustomfieldsetUpdate

class CustomfieldsetShowDb(BaseModel):
    data: CustomfieldsetDb

