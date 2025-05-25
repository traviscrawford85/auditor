from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomfieldShowIn(BaseModel):
    data: Any

class CustomfieldShowOut(BaseModel):
    data: Any

class CustomfieldShowUpdate(BaseModel):
    data: Any

class CustomfieldShowDb(BaseModel):
    data: Any

