from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class IdsresponseIn(BaseModel):
    data: List[int]

class IdsresponseOut(BaseModel):
    data: List[int]

class IdsresponseUpdate(BaseModel):
    data: List[int]

class IdsresponseDb(BaseModel):
    data: List[int]

