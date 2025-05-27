from typing import Optional

from pydantic import BaseModel


class MattercreaterequestdatagroupIn(BaseModel):
    id: Optional[str] = None

class MattercreaterequestdatagroupOut(BaseModel):
    id: Optional[str] = None

class MattercreaterequestdatagroupUpdate(BaseModel):
    id: Optional[str] = None

class MattercreaterequestdatagroupDb(BaseModel):
    id: Optional[str] = None

