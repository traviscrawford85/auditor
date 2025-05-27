
from pydantic import BaseModel

from .billtheme import BillthemeOut


class BillthemeShowIn(BaseModel):
    data: BillthemeIn

class BillthemeShowOut(BaseModel):
    data: BillthemeOut

class BillthemeShowUpdate(BaseModel):
    data: BillthemeUpdate

class BillthemeShowDb(BaseModel):
    data: BillthemeDb

