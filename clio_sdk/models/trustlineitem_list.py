from typing import List

from pydantic import BaseModel

from .trustlineitem import TrustlineitemOut


class TrustlineitemListIn(BaseModel):
    data: List[TrustlineitemIn]

class TrustlineitemListOut(BaseModel):
    data: List[TrustlineitemOut]

class TrustlineitemListUpdate(BaseModel):
    data: List[TrustlineitemUpdate]

class TrustlineitemListDb(BaseModel):
    data: List[TrustlineitemDb]

