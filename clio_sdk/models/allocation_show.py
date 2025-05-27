
from pydantic import BaseModel

from .allocation import AllocationOut


class AllocationShowIn(BaseModel):
    data: AllocationIn

class AllocationShowOut(BaseModel):
    data: AllocationOut

class AllocationShowUpdate(BaseModel):
    data: AllocationUpdate

class AllocationShowDb(BaseModel):
    data: AllocationDb

