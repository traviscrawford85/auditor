from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class UserShowIn(BaseModel):
    data: User

class UserShowOut(BaseModel):
    data: User

class UserShowUpdate(BaseModel):
    data: User

class UserShowDb(BaseModel):
    data: User

