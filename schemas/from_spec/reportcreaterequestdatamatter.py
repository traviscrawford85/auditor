from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ReportcreaterequestdatamatterIn(BaseModel):
    id: Optional[str] = None

class ReportcreaterequestdatamatterOut(BaseModel):
    id: Optional[str] = None

class ReportcreaterequestdatamatterUpdate(BaseModel):
    id: Optional[str] = None

class ReportcreaterequestdatamatterDb(BaseModel):
    id: Optional[str] = None

