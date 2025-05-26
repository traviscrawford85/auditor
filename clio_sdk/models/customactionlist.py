from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomactionListIn(BaseModel):
    data: List[Customaction]

class CustomactionListOut(BaseModel):
    data: List[Customaction]

class CustomactionListUpdate(BaseModel):
    data: List[Customaction]

class CustomactionListDb(BaseModel):
    data: List[Customaction]

