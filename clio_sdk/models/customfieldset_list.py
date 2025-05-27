from typing import List

from pydantic import BaseModel

from .customfieldset import CustomfieldsetOut


class CustomfieldsetListIn(BaseModel):
    data: List[CustomfieldsetIn]

class CustomfieldsetListOut(BaseModel):
    data: List[CustomfieldsetOut]

class CustomfieldsetListUpdate(BaseModel):
    data: List[CustomfieldsetUpdate]

class CustomfieldsetListDb(BaseModel):
    data: List[CustomfieldsetDb]

