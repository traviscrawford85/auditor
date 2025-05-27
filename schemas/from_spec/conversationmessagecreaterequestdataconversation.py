from typing import Optional

from pydantic import BaseModel


class ConversationmessagecreaterequestdataconversationIn(BaseModel):
    id: Optional[str] = None

class ConversationmessagecreaterequestdataconversationOut(BaseModel):
    id: Optional[str] = None

class ConversationmessagecreaterequestdataconversationUpdate(BaseModel):
    id: Optional[str] = None

class ConversationmessagecreaterequestdataconversationDb(BaseModel):
    id: Optional[str] = None

