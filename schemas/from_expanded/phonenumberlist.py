from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class PhonenumberListIn(BaseModel):
    data: List[Any]

class PhonenumberListOut(BaseModel):
    data: List[Any]

class PhonenumberListUpdate(BaseModel):
    data: List[Any]

class PhonenumberListDb(BaseModel):
    data: List[Any]

