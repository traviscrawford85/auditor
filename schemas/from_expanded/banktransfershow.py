from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BanktransferShowIn(BaseModel):
    data: Any

class BanktransferShowOut(BaseModel):
    data: Any

class BanktransferShowUpdate(BaseModel):
    data: Any

class BanktransferShowDb(BaseModel):
    data: Any

