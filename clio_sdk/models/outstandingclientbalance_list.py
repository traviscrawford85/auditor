from typing import List

from pydantic import BaseModel

from .outstandingclientbalance import OutstandingclientbalanceOut


class OutstandingclientbalanceListIn(BaseModel):
    data: List[OutstandingclientbalanceIn]

class OutstandingclientbalanceListOut(BaseModel):
    data: List[OutstandingclientbalanceOut]

class OutstandingclientbalanceListUpdate(BaseModel):
    data: List[OutstandingclientbalanceUpdate]

class OutstandingclientbalanceListDb(BaseModel):
    data: List[OutstandingclientbalanceDb]

