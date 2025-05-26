from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MultipartBaseIn(BaseModel):
    part_number: Optional[str] = None
    put_url: Optional[str] = None

class MultipartBaseOut(BaseModel):
    part_number: Optional[str] = None
    put_url: Optional[str] = None

class MultipartBaseUpdate(BaseModel):
    part_number: Optional[str] = None
    put_url: Optional[str] = None

class MultipartBaseDb(BaseModel):
    part_number: Optional[str] = None
    put_url: Optional[str] = None

