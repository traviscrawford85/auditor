from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportpresetcreaterequestdataIn(BaseModel):
    format: str
    kind: str
    name: str
    options: str

class ReportpresetcreaterequestdataOut(BaseModel):
    format: str
    kind: str
    name: str
    options: str

class ReportpresetcreaterequestdataUpdate(BaseModel):
    format: str
    kind: str
    name: str
    options: str

class ReportpresetcreaterequestdataDb(BaseModel):
    format: str
    kind: str
    name: str
    options: str

