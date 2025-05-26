from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class UserListIn(BaseModel):
    data: List[User]

class UserListOut(BaseModel):
    data: List[User]

class UserListUpdate(BaseModel):
    data: List[User]

class UserListDb(BaseModel):
    data: List[User]

