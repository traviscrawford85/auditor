from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterShowIn(BaseModel):
    data: Any

class MatterShowOut(BaseModel):
    data: Any

class MatterShowUpdate(BaseModel):
    data: Any

class MatterShowDb(BaseModel):
    data: Any

