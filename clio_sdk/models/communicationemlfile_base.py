from typing import Optional

from pydantic import BaseModel


class CommunicationemlfileBaseIn(BaseModel):
    id: Optional[int] = None

class CommunicationemlfileBaseOut(BaseModel):
    id: Optional[int] = None

class CommunicationemlfileBaseUpdate(BaseModel):
    id: Optional[int] = None

class CommunicationemlfileBaseDb(BaseModel):
    id: Optional[int] = None

