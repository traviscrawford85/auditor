from typing import List

from pydantic import BaseModel

from .cliopaymentslink import CliopaymentslinkOut


class CliopaymentslinkListIn(BaseModel):
    data: List[CliopaymentslinkIn]

class CliopaymentslinkListOut(BaseModel):
    data: List[CliopaymentslinkOut]

class CliopaymentslinkListUpdate(BaseModel):
    data: List[CliopaymentslinkUpdate]

class CliopaymentslinkListDb(BaseModel):
    data: List[CliopaymentslinkDb]

