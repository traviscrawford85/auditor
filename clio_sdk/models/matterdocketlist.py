from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterdocketListIn(BaseModel):
    data: List[Matterdocket]

class MatterdocketListOut(BaseModel):
    data: List[Matterdocket]

class MatterdocketListUpdate(BaseModel):
    data: List[Matterdocket]

class MatterdocketListDb(BaseModel):
    data: List[Matterdocket]

