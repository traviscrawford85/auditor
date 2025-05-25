from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomactionShowIn(BaseModel):
    data: Any

class CustomactionShowOut(BaseModel):
    data: Any

class CustomactionShowUpdate(BaseModel):
    data: Any

class CustomactionShowDb(BaseModel):
    data: Any

