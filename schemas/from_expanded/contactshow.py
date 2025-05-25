from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ContactShowIn(BaseModel):
    data: Any

class ContactShowOut(BaseModel):
    data: Any

class ContactShowUpdate(BaseModel):
    data: Any

class ContactShowDb(BaseModel):
    data: Any

