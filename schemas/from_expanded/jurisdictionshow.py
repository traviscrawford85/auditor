from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class JurisdictionShowIn(BaseModel):
    data: Any

class JurisdictionShowOut(BaseModel):
    data: Any

class JurisdictionShowUpdate(BaseModel):
    data: Any

class JurisdictionShowDb(BaseModel):
    data: Any

