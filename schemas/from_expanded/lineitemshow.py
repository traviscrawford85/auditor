from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LineitemShowIn(BaseModel):
    data: Any

class LineitemShowOut(BaseModel):
    data: Any

class LineitemShowUpdate(BaseModel):
    data: Any

class LineitemShowDb(BaseModel):
    data: Any

