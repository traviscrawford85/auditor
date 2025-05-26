from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ContactListIn(BaseModel):
    data: List[Contact]

class ContactListOut(BaseModel):
    data: List[Contact]

class ContactListUpdate(BaseModel):
    data: List[Contact]

class ContactListDb(BaseModel):
    data: List[Contact]

