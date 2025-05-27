from typing import Optional

from pydantic import BaseModel


class MattercreaterequestdatapracticeareaIn(BaseModel):
    id: Optional[str] = None

class MattercreaterequestdatapracticeareaOut(BaseModel):
    id: Optional[str] = None

class MattercreaterequestdatapracticeareaUpdate(BaseModel):
    id: Optional[str] = None

class MattercreaterequestdatapracticeareaDb(BaseModel):
    id: Optional[str] = None

