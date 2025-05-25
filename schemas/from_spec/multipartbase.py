from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MultipartbaseIn(BaseModel):
    part_number: Optional[str] = None
    put_url: Optional[str] = None

class MultipartbaseOut(BaseModel):
    part_number: Optional[str] = None
    put_url: Optional[str] = None

class MultipartbaseUpdate(BaseModel):
    part_number: Optional[str] = None
    put_url: Optional[str] = None

class MultipartbaseDb(BaseModel):
    part_number: Optional[str] = None
    put_url: Optional[str] = None

