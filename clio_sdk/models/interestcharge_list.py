from typing import List

from pydantic import BaseModel

from .interestcharge import InterestchargeOut


class InterestchargeListIn(BaseModel):
    data: List[InterestchargeIn]

class InterestchargeListOut(BaseModel):
    data: List[InterestchargeOut]

class InterestchargeListUpdate(BaseModel):
    data: List[InterestchargeUpdate]

class InterestchargeListDb(BaseModel):
    data: List[InterestchargeDb]

