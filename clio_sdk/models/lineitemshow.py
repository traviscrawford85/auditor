from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class LineitemShowIn(BaseModel):
    data: Lineitem

class LineitemShowOut(BaseModel):
    data: Lineitem

class LineitemShowUpdate(BaseModel):
    data: Lineitem

class LineitemShowDb(BaseModel):
    data: Lineitem

