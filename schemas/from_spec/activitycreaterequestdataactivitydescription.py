from typing import Optional

from pydantic import BaseModel


class ActivitycreaterequestdataactivitydescriptionIn(BaseModel):
    id: Optional[str] = None
    utbms_task_id: Optional[str] = None
    utbms_activity_id: Optional[str] = None

class ActivitycreaterequestdataactivitydescriptionOut(BaseModel):
    id: Optional[str] = None
    utbms_task_id: Optional[str] = None
    utbms_activity_id: Optional[str] = None

class ActivitycreaterequestdataactivitydescriptionUpdate(BaseModel):
    id: Optional[str] = None
    utbms_task_id: Optional[str] = None
    utbms_activity_id: Optional[str] = None

class ActivitycreaterequestdataactivitydescriptionDb(BaseModel):
    id: Optional[str] = None
    utbms_task_id: Optional[str] = None
    utbms_activity_id: Optional[str] = None

