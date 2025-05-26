from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class JurisdictionShowIn(BaseModel):
    data: Jurisdiction

class JurisdictionShowOut(BaseModel):
    data: Jurisdiction

class JurisdictionShowUpdate(BaseModel):
    data: Jurisdiction

class JurisdictionShowDb(BaseModel):
    data: Jurisdiction

