from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class EventmetricsbaseIn(BaseModel):
    unread_mobile_events: Optional[str] = None
    unread_web_events: Optional[str] = None
    unread_secure_messages: Optional[str] = None
    unread_client_portal_messages: Optional[str] = None
    unread_text_messages: Optional[str] = None

class EventmetricsbaseOut(BaseModel):
    unread_mobile_events: Optional[str] = None
    unread_web_events: Optional[str] = None
    unread_secure_messages: Optional[str] = None
    unread_client_portal_messages: Optional[str] = None
    unread_text_messages: Optional[str] = None

class EventmetricsbaseUpdate(BaseModel):
    unread_mobile_events: Optional[str] = None
    unread_web_events: Optional[str] = None
    unread_secure_messages: Optional[str] = None
    unread_client_portal_messages: Optional[str] = None
    unread_text_messages: Optional[str] = None

class EventmetricsbaseDb(BaseModel):
    unread_mobile_events: Optional[str] = None
    unread_web_events: Optional[str] = None
    unread_secure_messages: Optional[str] = None
    unread_client_portal_messages: Optional[str] = None
    unread_text_messages: Optional[str] = None

