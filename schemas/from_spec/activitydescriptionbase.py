from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ActivitydescriptionbaseIn(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    visible_to_co_counsel: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    default: Optional[str] = None
    type: Optional[str] = None
    utbms_activity_id: Optional[str] = None
    utbms_task_name: Optional[str] = None
    utbms_task_id: Optional[str] = None
    xero_service_code: Optional[str] = None
    accessible_to_user: Optional[str] = None
    category_type: Optional[str] = None
    currency: Optional[str] = None

class ActivitydescriptionbaseOut(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    visible_to_co_counsel: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    default: Optional[str] = None
    type: Optional[str] = None
    utbms_activity_id: Optional[str] = None
    utbms_task_name: Optional[str] = None
    utbms_task_id: Optional[str] = None
    xero_service_code: Optional[str] = None
    accessible_to_user: Optional[str] = None
    category_type: Optional[str] = None
    currency: Optional[str] = None

class ActivitydescriptionbaseUpdate(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    visible_to_co_counsel: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    default: Optional[str] = None
    type: Optional[str] = None
    utbms_activity_id: Optional[str] = None
    utbms_task_name: Optional[str] = None
    utbms_task_id: Optional[str] = None
    xero_service_code: Optional[str] = None
    accessible_to_user: Optional[str] = None
    category_type: Optional[str] = None
    currency: Optional[str] = None

class ActivitydescriptionbaseDb(BaseModel):
    id: Optional[str] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    visible_to_co_counsel: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    default: Optional[str] = None
    type: Optional[str] = None
    utbms_activity_id: Optional[str] = None
    utbms_task_name: Optional[str] = None
    utbms_task_id: Optional[str] = None
    xero_service_code: Optional[str] = None
    accessible_to_user: Optional[str] = None
    category_type: Optional[str] = None
    currency: Optional[str] = None

