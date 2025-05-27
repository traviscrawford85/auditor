from typing import Optional

from pydantic import BaseModel


class ReportpresetupdaterequestdataIn(BaseModel):
    format: Optional[str] = None
    kind: Optional[str] = None
    name: Optional[str] = None
    options: Optional[str] = None

class ReportpresetupdaterequestdataOut(BaseModel):
    format: Optional[str] = None
    kind: Optional[str] = None
    name: Optional[str] = None
    options: Optional[str] = None

class ReportpresetupdaterequestdataUpdate(BaseModel):
    format: Optional[str] = None
    kind: Optional[str] = None
    name: Optional[str] = None
    options: Optional[str] = None

class ReportpresetupdaterequestdataDb(BaseModel):
    format: Optional[str] = None
    kind: Optional[str] = None
    name: Optional[str] = None
    options: Optional[str] = None

