from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DamageShowIn(BaseModel):
    data: Any

class DamageShowOut(BaseModel):
    data: Any

class DamageShowUpdate(BaseModel):
    data: Any

class DamageShowDb(BaseModel):
    data: Any

