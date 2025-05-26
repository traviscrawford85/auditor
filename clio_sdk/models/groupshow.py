from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class GroupShowIn(BaseModel):
    data: Group

class GroupShowOut(BaseModel):
    data: Group

class GroupShowUpdate(BaseModel):
    data: Group

class GroupShowDb(BaseModel):
    data: Group

