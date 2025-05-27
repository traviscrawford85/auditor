from typing import List

from pydantic import BaseModel

from .communication import CommunicationOut


class CommunicationListIn(BaseModel):
    data: List[CommunicationIn]

class CommunicationListOut(BaseModel):
    data: List[CommunicationOut]

class CommunicationListUpdate(BaseModel):
    data: List[CommunicationUpdate]

class CommunicationListDb(BaseModel):
    data: List[CommunicationDb]

