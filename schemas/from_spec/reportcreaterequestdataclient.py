from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportcreaterequestdataclientIn(BaseModel):
    id: Optional[str] = None

class ReportcreaterequestdataclientOut(BaseModel):
    id: Optional[str] = None

class ReportcreaterequestdataclientUpdate(BaseModel):
    id: Optional[str] = None

class ReportcreaterequestdataclientDb(BaseModel):
    id: Optional[str] = None

