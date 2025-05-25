from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TrustlineitemShowIn(BaseModel):
    data: Any

class TrustlineitemShowOut(BaseModel):
    data: Any

class TrustlineitemShowUpdate(BaseModel):
    data: Any

class TrustlineitemShowDb(BaseModel):
    data: Any

