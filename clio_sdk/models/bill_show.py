
from pydantic import BaseModel

from .bill import BillOut


class BillShowIn(BaseModel):
    data: BillIn

class BillShowOut(BaseModel):
    data: BillOut

class BillShowUpdate(BaseModel):
    data: BillUpdate

class BillShowDb(BaseModel):
    data: BillDb

