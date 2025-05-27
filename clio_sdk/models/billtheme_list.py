from typing import List

from pydantic import BaseModel

from .billtheme import BillthemeOut


class BillthemeListIn(BaseModel):
    data: List[BillthemeIn]

class BillthemeListOut(BaseModel):
    data: List[BillthemeOut]

class BillthemeListUpdate(BaseModel):
    data: List[BillthemeUpdate]

class BillthemeListDb(BaseModel):
    data: List[BillthemeDb]

