from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CreditmemoShowIn(BaseModel):
    data: Any

class CreditmemoShowOut(BaseModel):
    data: Any

class CreditmemoShowUpdate(BaseModel):
    data: Any

class CreditmemoShowDb(BaseModel):
    data: Any

