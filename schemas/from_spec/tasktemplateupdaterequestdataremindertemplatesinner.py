from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TasktemplateupdaterequestdataremindertemplatesinnerIn(BaseModel):
    duration_value: Optional[str] = None
    duration_unit: Optional[str] = None
    notification_type: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

class TasktemplateupdaterequestdataremindertemplatesinnerOut(BaseModel):
    duration_value: Optional[str] = None
    duration_unit: Optional[str] = None
    notification_type: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

class TasktemplateupdaterequestdataremindertemplatesinnerUpdate(BaseModel):
    duration_value: Optional[str] = None
    duration_unit: Optional[str] = None
    notification_type: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

class TasktemplateupdaterequestdataremindertemplatesinnerDb(BaseModel):
    duration_value: Optional[str] = None
    duration_unit: Optional[str] = None
    notification_type: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

