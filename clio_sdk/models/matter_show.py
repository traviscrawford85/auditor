
from pydantic import BaseModel

from .matter import MatterOut


class MatterShowIn(BaseModel):
    data: MatterIn

class MatterShowOut(BaseModel):
    data: MatterOut

class MatterShowUpdate(BaseModel):
    data: MatterUpdate

class MatterShowDb(BaseModel):
    data: MatterDb

