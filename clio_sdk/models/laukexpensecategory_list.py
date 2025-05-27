from typing import List

from pydantic import BaseModel

from .laukexpensecategory import LaukexpensecategoryOut


class LaukexpensecategoryListIn(BaseModel):
    data: List[LaukexpensecategoryIn]

class LaukexpensecategoryListOut(BaseModel):
    data: List[LaukexpensecategoryOut]

class LaukexpensecategoryListUpdate(BaseModel):
    data: List[LaukexpensecategoryUpdate]

class LaukexpensecategoryListDb(BaseModel):
    data: List[LaukexpensecategoryDb]

