from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class GrantShowIn(BaseModel):
    data: Any

class GrantShowOut(BaseModel):
    data: Any

class GrantShowUpdate(BaseModel):
    data: Any

class GrantShowDb(BaseModel):
    data: Any

