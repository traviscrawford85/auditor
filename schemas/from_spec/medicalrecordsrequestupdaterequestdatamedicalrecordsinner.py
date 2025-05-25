from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MedicalrecordsrequestupdaterequestdatamedicalrecordsinnerIn(BaseModel):
    document_id: Optional[str] = None
    end_date: Optional[str] = None
    start_date: Optional[str] = None

class MedicalrecordsrequestupdaterequestdatamedicalrecordsinnerOut(BaseModel):
    document_id: Optional[str] = None
    end_date: Optional[str] = None
    start_date: Optional[str] = None

class MedicalrecordsrequestupdaterequestdatamedicalrecordsinnerUpdate(BaseModel):
    document_id: Optional[str] = None
    end_date: Optional[str] = None
    start_date: Optional[str] = None

class MedicalrecordsrequestupdaterequestdatamedicalrecordsinnerDb(BaseModel):
    document_id: Optional[str] = None
    end_date: Optional[str] = None
    start_date: Optional[str] = None

