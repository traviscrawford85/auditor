from typing import List

from pydantic import BaseModel

from .damage import DamageOut


class DamageListIn(BaseModel):
    data: List[DamageIn]

class DamageListOut(BaseModel):
    data: List[DamageOut]

class DamageListUpdate(BaseModel):
    data: List[DamageUpdate]

class DamageListDb(BaseModel):
    data: List[DamageDb]

