from typing import Optional

from pydantic import BaseModel


class EventmetricsIn(BaseModel):
    unread_mobile_events: Optional[str] = None
    unread_web_events: Optional[str] = None
    unread_secure_messages: Optional[str] = None
    unread_client_portal_messages: Optional[str] = None
    unread_text_messages: Optional[str] = None

class EventmetricsOut(BaseModel):
    unread_mobile_events: Optional[str] = None
    unread_web_events: Optional[str] = None
    unread_secure_messages: Optional[str] = None
    unread_client_portal_messages: Optional[str] = None
    unread_text_messages: Optional[str] = None

class EventmetricsUpdate(BaseModel):
    unread_mobile_events: Optional[str] = None
    unread_web_events: Optional[str] = None
    unread_secure_messages: Optional[str] = None
    unread_client_portal_messages: Optional[str] = None
    unread_text_messages: Optional[str] = None

class EventmetricsDb(BaseModel):
    unread_mobile_events: Optional[str] = None
    unread_web_events: Optional[str] = None
    unread_secure_messages: Optional[str] = None
    unread_client_portal_messages: Optional[str] = None
    unread_text_messages: Optional[str] = None

