from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class GroupShowIn(BaseModel):
    data: Any

class GroupShowOut(BaseModel):
    data: Any

class GroupShowUpdate(BaseModel):
    data: Any

class GroupShowDb(BaseModel):
    data: Any

