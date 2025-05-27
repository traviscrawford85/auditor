from typing import Optional

from pydantic import BaseModel


class ActivityTextmessageconversationBaseIn(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None

class ActivityTextmessageconversationBaseOut(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None

class ActivityTextmessageconversationBaseUpdate(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None

class ActivityTextmessageconversationBaseDb(BaseModel):
    id: Optional[int] = None
    etag: Optional[str] = None

