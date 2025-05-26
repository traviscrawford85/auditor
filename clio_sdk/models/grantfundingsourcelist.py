from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class GrantfundingsourceListIn(BaseModel):
    data: List[Grantfundingsource]

class GrantfundingsourceListOut(BaseModel):
    data: List[Grantfundingsource]

class GrantfundingsourceListUpdate(BaseModel):
    data: List[Grantfundingsource]

class GrantfundingsourceListDb(BaseModel):
    data: List[Grantfundingsource]

