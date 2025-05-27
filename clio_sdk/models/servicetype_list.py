from typing import List

from pydantic import BaseModel

from .servicetype import ServicetypeOut


class ServicetypeListIn(BaseModel):
    data: List[ServicetypeIn]

class ServicetypeListOut(BaseModel):
    data: List[ServicetypeOut]

class ServicetypeListUpdate(BaseModel):
    data: List[ServicetypeUpdate]

class ServicetypeListDb(BaseModel):
    data: List[ServicetypeDb]

