from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

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

