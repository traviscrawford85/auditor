from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BanktransactionShowIn(BaseModel):
    data: Any

class BanktransactionShowOut(BaseModel):
    data: Any

class BanktransactionShowUpdate(BaseModel):
    data: Any

class BanktransactionShowDb(BaseModel):
    data: Any

