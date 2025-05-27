from typing import List

from pydantic import BaseModel

from .cliopaymentspayment import CliopaymentspaymentOut


class CliopaymentspaymentListIn(BaseModel):
    data: List[CliopaymentspaymentIn]

class CliopaymentspaymentListOut(BaseModel):
    data: List[CliopaymentspaymentOut]

class CliopaymentspaymentListUpdate(BaseModel):
    data: List[CliopaymentspaymentUpdate]

class CliopaymentspaymentListDb(BaseModel):
    data: List[CliopaymentspaymentDb]

