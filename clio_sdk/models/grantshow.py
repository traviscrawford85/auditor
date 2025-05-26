from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class GrantShowIn(BaseModel):
    data: Grant

class GrantShowOut(BaseModel):
    data: Grant

class GrantShowUpdate(BaseModel):
    data: Grant

class GrantShowDb(BaseModel):
    data: Grant

