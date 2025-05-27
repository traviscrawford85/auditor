from typing import Optional

from pydantic import BaseModel


class GroupcreaterequestdataIn(BaseModel):
    name: Optional[str] = None

class GroupcreaterequestdataOut(BaseModel):
    name: Optional[str] = None

class GroupcreaterequestdataUpdate(BaseModel):
    name: Optional[str] = None

class GroupcreaterequestdataDb(BaseModel):
    name: Optional[str] = None

