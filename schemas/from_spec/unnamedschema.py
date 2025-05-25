from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class UnnamedschemaIn(BaseModel):
    name: Optional[Any] = None
    value: Optional[Any] = None

class UnnamedschemaOut(BaseModel):
    name: Optional[Any] = None
    value: Optional[Any] = None

class UnnamedschemaUpdate(BaseModel):
    name: Optional[Any] = None
    value: Optional[Any] = None

class UnnamedschemaDb(BaseModel):
    name: Optional[Any] = None
    value: Optional[Any] = None

