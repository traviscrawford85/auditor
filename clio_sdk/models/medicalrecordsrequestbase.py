from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MedicalrecordsrequestBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    bills_follow_up_date: Optional[datetime] = None
    bills_request_date: Optional[datetime] = None
    bills_status: Optional[str] = None
    description: Optional[str] = None
    in_treatment: Optional[bool] = None
    records_follow_up_date: Optional[datetime] = None
    records_request_date: Optional[datetime] = None
    records_status: Optional[str] = None
    treatment_end_date: Optional[datetime] = None
    treatment_start_date: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class MedicalrecordsrequestBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    bills_follow_up_date: Optional[datetime] = None
    bills_request_date: Optional[datetime] = None
    bills_status: Optional[str] = None
    description: Optional[str] = None
    in_treatment: Optional[bool] = None
    records_follow_up_date: Optional[datetime] = None
    records_request_date: Optional[datetime] = None
    records_status: Optional[str] = None
    treatment_end_date: Optional[datetime] = None
    treatment_start_date: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class MedicalrecordsrequestBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    bills_follow_up_date: Optional[datetime] = None
    bills_request_date: Optional[datetime] = None
    bills_status: Optional[str] = None
    description: Optional[str] = None
    in_treatment: Optional[bool] = None
    records_follow_up_date: Optional[datetime] = None
    records_request_date: Optional[datetime] = None
    records_status: Optional[str] = None
    treatment_end_date: Optional[datetime] = None
    treatment_start_date: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class MedicalrecordsrequestBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    bills_follow_up_date: Optional[datetime] = None
    bills_request_date: Optional[datetime] = None
    bills_status: Optional[str] = None
    description: Optional[str] = None
    in_treatment: Optional[bool] = None
    records_follow_up_date: Optional[datetime] = None
    records_request_date: Optional[datetime] = None
    records_status: Optional[str] = None
    treatment_end_date: Optional[datetime] = None
    treatment_start_date: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

