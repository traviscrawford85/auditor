from typing import Optional

from pydantic import BaseModel


class ActivitydescriptionBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    visible_to_co_counsel: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    default: Optional[bool] = None
    type: Optional[str] = None
    utbms_activity_id: Optional[int] = None
    utbms_task_name: Optional[str] = None
    utbms_task_id: Optional[int] = None
    xero_service_code: Optional[str] = None
    accessible_to_user: Optional[bool] = None
    category_type: Optional[str] = None

class ActivitydescriptionBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    visible_to_co_counsel: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    default: Optional[bool] = None
    type: Optional[str] = None
    utbms_activity_id: Optional[int] = None
    utbms_task_name: Optional[str] = None
    utbms_task_id: Optional[int] = None
    xero_service_code: Optional[str] = None
    accessible_to_user: Optional[bool] = None
    category_type: Optional[str] = None

class ActivitydescriptionBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    visible_to_co_counsel: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    default: Optional[bool] = None
    type: Optional[str] = None
    utbms_activity_id: Optional[int] = None
    utbms_task_name: Optional[str] = None
    utbms_task_id: Optional[int] = None
    xero_service_code: Optional[str] = None
    accessible_to_user: Optional[bool] = None
    category_type: Optional[str] = None

class ActivitydescriptionBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    visible_to_co_counsel: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    default: Optional[bool] = None
    type: Optional[str] = None
    utbms_activity_id: Optional[int] = None
    utbms_task_name: Optional[str] = None
    utbms_task_id: Optional[int] = None
    xero_service_code: Optional[str] = None
    accessible_to_user: Optional[bool] = None
    category_type: Optional[str] = None

