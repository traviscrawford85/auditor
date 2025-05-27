from typing import List

from pydantic import BaseModel

from .creditmemo import CreditmemoOut


class CreditmemoListIn(BaseModel):
    data: List[CreditmemoIn]

class CreditmemoListOut(BaseModel):
    data: List[CreditmemoOut]

class CreditmemoListUpdate(BaseModel):
    data: List[CreditmemoUpdate]

class CreditmemoListDb(BaseModel):
    data: List[CreditmemoDb]

