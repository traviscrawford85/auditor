from typing import List

from pydantic import BaseModel

from .billableclient import BillableclientOut


class BillableclientListIn(BaseModel):
    data: List[BillableclientIn]

class BillableclientListOut(BaseModel):
    data: List[BillableclientOut]

class BillableclientListUpdate(BaseModel):
    data: List[BillableclientUpdate]

class BillableclientListDb(BaseModel):
    data: List[BillableclientDb]

