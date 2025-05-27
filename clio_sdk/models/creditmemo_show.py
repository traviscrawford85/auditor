
from pydantic import BaseModel

from .creditmemo import CreditmemoOut


class CreditmemoShowIn(BaseModel):
    data: CreditmemoIn

class CreditmemoShowOut(BaseModel):
    data: CreditmemoOut

class CreditmemoShowUpdate(BaseModel):
    data: CreditmemoUpdate

class CreditmemoShowDb(BaseModel):
    data: CreditmemoDb

