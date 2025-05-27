
from pydantic import BaseModel

from .damage import DamageOut


class DamageShowIn(BaseModel):
    data: DamageIn

class DamageShowOut(BaseModel):
    data: DamageOut

class DamageShowUpdate(BaseModel):
    data: DamageUpdate

class DamageShowDb(BaseModel):
    data: DamageDb

