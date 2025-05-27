from typing import List

from pydantic import BaseModel

from .item import ItemOut


class ItemListIn(BaseModel):
    data: List[ItemIn]

class ItemListOut(BaseModel):
    data: List[ItemOut]

class ItemListUpdate(BaseModel):
    data: List[ItemUpdate]

class ItemListDb(BaseModel):
    data: List[ItemDb]

