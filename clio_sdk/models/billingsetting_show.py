
from pydantic import BaseModel

from .billingsetting import BillingsettingOut


class BillingsettingShowIn(BaseModel):
    data: BillingsettingIn

class BillingsettingShowOut(BaseModel):
    data: BillingsettingOut

class BillingsettingShowUpdate(BaseModel):
    data: BillingsettingUpdate

class BillingsettingShowDb(BaseModel):
    data: BillingsettingDb

