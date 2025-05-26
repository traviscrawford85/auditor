from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class DamageShowIn(BaseModel):
    data: Damage

class DamageShowOut(BaseModel):
    data: Damage

class DamageShowUpdate(BaseModel):
    data: Damage

class DamageShowDb(BaseModel):
    data: Damage

