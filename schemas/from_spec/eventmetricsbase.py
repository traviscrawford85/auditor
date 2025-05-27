from typing import Optional

from pydantic import BaseModel


class EventmetricsBaseIn(BaseModel):
    unread_mobile_events: Optional[str] = None
    unread_web_events: Optional[str] = None
    unread_secure_messages: Optional[str] = None
    unread_client_portal_messages: Optional[str] = None
    unread_text_messages: Optional[str] = None

class EventmetricsBaseOut(BaseModel):
    unread_mobile_events: Optional[str] = None
    unread_web_events: Optional[str] = None
    unread_secure_messages: Optional[str] = None
    unread_client_portal_messages: Optional[str] = None
    unread_text_messages: Optional[str] = None

class EventmetricsBaseUpdate(BaseModel):
    unread_mobile_events: Optional[str] = None
    unread_web_events: Optional[str] = None
    unread_secure_messages: Optional[str] = None
    unread_client_portal_messages: Optional[str] = None
    unread_text_messages: Optional[str] = None

class EventmetricsBaseDb(BaseModel):
    unread_mobile_events: Optional[str] = None
    unread_web_events: Optional[str] = None
    unread_secure_messages: Optional[str] = None
    unread_client_portal_messages: Optional[str] = None
    unread_text_messages: Optional[str] = None

