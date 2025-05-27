from typing import List

from pydantic import BaseModel

from .bill import BillOut


class BillListIn(BaseModel):
    data: List[BillIn]

class BillListOut(BaseModel):
    data: List[BillOut]

class BillListUpdate(BaseModel):
    data: List[BillUpdate]

class BillListDb(BaseModel):
    data: List[BillDb]

