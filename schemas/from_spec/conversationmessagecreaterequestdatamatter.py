from typing import Optional

from pydantic import BaseModel


class ConversationmessagecreaterequestdatamatterIn(BaseModel):
    id: Optional[str] = None

class ConversationmessagecreaterequestdatamatterOut(BaseModel):
    id: Optional[str] = None

class ConversationmessagecreaterequestdatamatterUpdate(BaseModel):
    id: Optional[str] = None

class ConversationmessagecreaterequestdatamatterDb(BaseModel):
    id: Optional[str] = None

