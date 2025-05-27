from typing import Optional

from pydantic import BaseModel


class ConversationupdaterequestdatamatterIn(BaseModel):
    id: Optional[str] = None

class ConversationupdaterequestdatamatterOut(BaseModel):
    id: Optional[str] = None

class ConversationupdaterequestdatamatterUpdate(BaseModel):
    id: Optional[str] = None

class ConversationupdaterequestdatamatterDb(BaseModel):
    id: Optional[str] = None

