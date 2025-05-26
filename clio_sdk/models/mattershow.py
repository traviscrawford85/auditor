from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MatterShowIn(BaseModel):
    data: Matter

class MatterShowOut(BaseModel):
    data: Matter

class MatterShowUpdate(BaseModel):
    data: Matter

class MatterShowDb(BaseModel):
    data: Matter

