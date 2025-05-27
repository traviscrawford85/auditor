
from pydantic import BaseModel

from .servicetype import ServicetypeOut


class ServicetypeShowIn(BaseModel):
    data: ServicetypeIn

class ServicetypeShowOut(BaseModel):
    data: ServicetypeOut

class ServicetypeShowUpdate(BaseModel):
    data: ServicetypeUpdate

class ServicetypeShowDb(BaseModel):
    data: ServicetypeDb

