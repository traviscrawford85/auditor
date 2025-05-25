from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class UserListIn(BaseModel):
    data: List[Any]

class UserListOut(BaseModel):
    data: List[Any]

class UserListUpdate(BaseModel):
    data: List[Any]

class UserListDb(BaseModel):
    data: List[Any]

