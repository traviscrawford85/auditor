
from pydantic import BaseModel

from .cliopaymentspayment import CliopaymentspaymentOut


class CliopaymentspaymentShowIn(BaseModel):
    data: CliopaymentspaymentIn

class CliopaymentspaymentShowOut(BaseModel):
    data: CliopaymentspaymentOut

class CliopaymentspaymentShowUpdate(BaseModel):
    data: CliopaymentspaymentUpdate

class CliopaymentspaymentShowDb(BaseModel):
    data: CliopaymentspaymentDb

