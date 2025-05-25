from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ContactListIn(BaseModel):
    data: List[Any]

class ContactListOut(BaseModel):
    data: List[Any]

class ContactListUpdate(BaseModel):
    data: List[Any]

class ContactListDb(BaseModel):
    data: List[Any]

