from typing import List

from pydantic import BaseModel

from .billablematter import BillablematterOut


class BillablematterListIn(BaseModel):
    data: List[BillablematterIn]

class BillablematterListOut(BaseModel):
    data: List[BillablematterOut]

class BillablematterListUpdate(BaseModel):
    data: List[BillablematterUpdate]

class BillablematterListDb(BaseModel):
    data: List[BillablematterDb]

