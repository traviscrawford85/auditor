from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CliopaymentslinkListIn(BaseModel):
    data: List[Any]

class CliopaymentslinkListOut(BaseModel):
    data: List[Any]

class CliopaymentslinkListUpdate(BaseModel):
    data: List[Any]

class CliopaymentslinkListDb(BaseModel):
    data: List[Any]

