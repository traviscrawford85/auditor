from typing import Optional

from pydantic import BaseModel


class EventmetricsBaseIn(BaseModel):
    unread_mobile_events: Optional[int] = None
    unread_web_events: Optional[int] = None
    unread_secure_messages: Optional[int] = None
    unread_client_portal_messages: Optional[int] = None
    unread_text_messages: Optional[int] = None

class EventmetricsBaseOut(BaseModel):
    unread_mobile_events: Optional[int] = None
    unread_web_events: Optional[int] = None
    unread_secure_messages: Optional[int] = None
    unread_client_portal_messages: Optional[int] = None
    unread_text_messages: Optional[int] = None

class EventmetricsBaseUpdate(BaseModel):
    unread_mobile_events: Optional[int] = None
    unread_web_events: Optional[int] = None
    unread_secure_messages: Optional[int] = None
    unread_client_portal_messages: Optional[int] = None
    unread_text_messages: Optional[int] = None

class EventmetricsBaseDb(BaseModel):
    unread_mobile_events: Optional[int] = None
    unread_web_events: Optional[int] = None
    unread_secure_messages: Optional[int] = None
    unread_client_portal_messages: Optional[int] = None
    unread_text_messages: Optional[int] = None

