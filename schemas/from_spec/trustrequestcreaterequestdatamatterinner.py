from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TrustrequestcreaterequestdatamatterinnerIn(BaseModel):
    id: Optional[str] = None
    trust_amount: Optional[str] = None
    note: Optional[str] = None

class TrustrequestcreaterequestdatamatterinnerOut(BaseModel):
    id: Optional[str] = None
    trust_amount: Optional[str] = None
    note: Optional[str] = None

class TrustrequestcreaterequestdatamatterinnerUpdate(BaseModel):
    id: Optional[str] = None
    trust_amount: Optional[str] = None
    note: Optional[str] = None

class TrustrequestcreaterequestdatamatterinnerDb(BaseModel):
    id: Optional[str] = None
    trust_amount: Optional[str] = None
    note: Optional[str] = None

