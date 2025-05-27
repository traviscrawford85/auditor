
from pydantic import BaseModel

from .trustlineitem import TrustlineitemOut


class TrustlineitemShowIn(BaseModel):
    data: TrustlineitemIn

class TrustlineitemShowOut(BaseModel):
    data: TrustlineitemOut

class TrustlineitemShowUpdate(BaseModel):
    data: TrustlineitemUpdate

class TrustlineitemShowDb(BaseModel):
    data: TrustlineitemDb

