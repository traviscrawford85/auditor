from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CustomfieldsetShowIn(BaseModel):
    data: Any

class CustomfieldsetShowOut(BaseModel):
    data: Any

class CustomfieldsetShowUpdate(BaseModel):
    data: Any

class CustomfieldsetShowDb(BaseModel):
    data: Any

