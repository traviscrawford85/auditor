from typing import Optional

from pydantic import BaseModel


class MedicalrecordsrequestBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    bills_follow_up_date: Optional[str] = None
    bills_request_date: Optional[str] = None
    bills_status: Optional[str] = None
    description: Optional[str] = None
    in_treatment: Optional[bool] = None
    records_follow_up_date: Optional[str] = None
    records_request_date: Optional[str] = None
    records_status: Optional[str] = None
    treatment_end_date: Optional[str] = None
    treatment_start_date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MedicalrecordsrequestBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    bills_follow_up_date: Optional[str] = None
    bills_request_date: Optional[str] = None
    bills_status: Optional[str] = None
    description: Optional[str] = None
    in_treatment: Optional[bool] = None
    records_follow_up_date: Optional[str] = None
    records_request_date: Optional[str] = None
    records_status: Optional[str] = None
    treatment_end_date: Optional[str] = None
    treatment_start_date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MedicalrecordsrequestBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    bills_follow_up_date: Optional[str] = None
    bills_request_date: Optional[str] = None
    bills_status: Optional[str] = None
    description: Optional[str] = None
    in_treatment: Optional[bool] = None
    records_follow_up_date: Optional[str] = None
    records_request_date: Optional[str] = None
    records_status: Optional[str] = None
    treatment_end_date: Optional[str] = None
    treatment_start_date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class MedicalrecordsrequestBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    bills_follow_up_date: Optional[str] = None
    bills_request_date: Optional[str] = None
    bills_status: Optional[str] = None
    description: Optional[str] = None
    in_treatment: Optional[bool] = None
    records_follow_up_date: Optional[str] = None
    records_request_date: Optional[str] = None
    records_status: Optional[str] = None
    treatment_end_date: Optional[str] = None
    treatment_start_date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

