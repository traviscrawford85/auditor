from typing import Optional

from pydantic import BaseModel


class TrustlineitemupdaterequestdataIn(BaseModel):
    date: Optional[str] = None
    note: Optional[str] = None
    total: Optional[str] = None

class TrustlineitemupdaterequestdataOut(BaseModel):
    date: Optional[str] = None
    note: Optional[str] = None
    total: Optional[str] = None

class TrustlineitemupdaterequestdataUpdate(BaseModel):
    date: Optional[str] = None
    note: Optional[str] = None
    total: Optional[str] = None

class TrustlineitemupdaterequestdataDb(BaseModel):
    date: Optional[str] = None
    note: Optional[str] = None
    total: Optional[str] = None

