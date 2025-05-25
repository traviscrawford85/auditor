from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class UserShowIn(BaseModel):
    data: Any

class UserShowOut(BaseModel):
    data: Any

class UserShowUpdate(BaseModel):
    data: Any

class UserShowDb(BaseModel):
    data: Any

