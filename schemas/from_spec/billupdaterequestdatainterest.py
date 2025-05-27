from typing import Optional

from pydantic import BaseModel


class BillupdaterequestdatainterestIn(BaseModel):
    rate: Optional[str] = None
    type: Optional[str] = None
    period: Optional[str] = None

class BillupdaterequestdatainterestOut(BaseModel):
    rate: Optional[str] = None
    type: Optional[str] = None
    period: Optional[str] = None

class BillupdaterequestdatainterestUpdate(BaseModel):
    rate: Optional[str] = None
    type: Optional[str] = None
    period: Optional[str] = None

class BillupdaterequestdatainterestDb(BaseModel):
    rate: Optional[str] = None
    type: Optional[str] = None
    period: Optional[str] = None

