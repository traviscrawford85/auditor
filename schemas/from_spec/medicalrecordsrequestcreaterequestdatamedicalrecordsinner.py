from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MedicalrecordsrequestcreaterequestdatamedicalrecordsinnerIn(BaseModel):
    document_id: int
    end_date: Optional[str] = None
    start_date: Optional[str] = None

class MedicalrecordsrequestcreaterequestdatamedicalrecordsinnerOut(BaseModel):
    document_id: int
    end_date: Optional[str] = None
    start_date: Optional[str] = None

class MedicalrecordsrequestcreaterequestdatamedicalrecordsinnerUpdate(BaseModel):
    document_id: int
    end_date: Optional[str] = None
    start_date: Optional[str] = None

class MedicalrecordsrequestcreaterequestdatamedicalrecordsinnerDb(BaseModel):
    document_id: int
    end_date: Optional[str] = None
    start_date: Optional[str] = None

