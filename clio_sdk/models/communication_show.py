
from pydantic import BaseModel

from .communication import CommunicationOut


class CommunicationShowIn(BaseModel):
    data: CommunicationIn

class CommunicationShowOut(BaseModel):
    data: CommunicationOut

class CommunicationShowUpdate(BaseModel):
    data: CommunicationUpdate

class CommunicationShowDb(BaseModel):
    data: CommunicationDb

