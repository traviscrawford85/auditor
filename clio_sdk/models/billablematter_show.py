
from pydantic import BaseModel

from .billablematter import BillablematterOut


class BillablematterShowIn(BaseModel):
    data: BillablematterIn

class BillablematterShowOut(BaseModel):
    data: BillablematterOut

class BillablematterShowUpdate(BaseModel):
    data: BillablematterUpdate

class BillablematterShowDb(BaseModel):
    data: BillablematterDb

