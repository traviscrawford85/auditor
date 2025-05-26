from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TrustlineitemShowIn(BaseModel):
    data: Trustlineitem

class TrustlineitemShowOut(BaseModel):
    data: Trustlineitem

class TrustlineitemShowUpdate(BaseModel):
    data: Trustlineitem

class TrustlineitemShowDb(BaseModel):
    data: Trustlineitem

