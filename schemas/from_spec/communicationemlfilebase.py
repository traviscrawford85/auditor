from typing import Optional

from pydantic import BaseModel


class CommunicationemlfileBaseIn(BaseModel):
    id: Optional[str] = None

class CommunicationemlfileBaseOut(BaseModel):
    id: Optional[str] = None

class CommunicationemlfileBaseUpdate(BaseModel):
    id: Optional[str] = None

class CommunicationemlfileBaseDb(BaseModel):
    id: Optional[str] = None

