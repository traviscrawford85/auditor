
from pydantic import BaseModel

from .client import ClientOut


class ClientShowIn(BaseModel):
    data: ClientIn

class ClientShowOut(BaseModel):
    data: ClientOut

class ClientShowUpdate(BaseModel):
    data: ClientUpdate

class ClientShowDb(BaseModel):
    data: ClientDb

