from typing import Optional

from pydantic import BaseModel


class ConversationmessagecreaterequestdataattachmentIn(BaseModel):
    document_id: Optional[str] = None
    document_version_id: Optional[str] = None

class ConversationmessagecreaterequestdataattachmentOut(BaseModel):
    document_id: Optional[str] = None
    document_version_id: Optional[str] = None

class ConversationmessagecreaterequestdataattachmentUpdate(BaseModel):
    document_id: Optional[str] = None
    document_version_id: Optional[str] = None

class ConversationmessagecreaterequestdataattachmentDb(BaseModel):
    document_id: Optional[str] = None
    document_version_id: Optional[str] = None

