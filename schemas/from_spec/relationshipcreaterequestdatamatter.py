from typing import Optional

from pydantic import BaseModel


class RelationshipcreaterequestdatamatterIn(BaseModel):
    id: Optional[str] = None

class RelationshipcreaterequestdatamatterOut(BaseModel):
    id: Optional[str] = None

class RelationshipcreaterequestdatamatterUpdate(BaseModel):
    id: Optional[str] = None

class RelationshipcreaterequestdatamatterDb(BaseModel):
    id: Optional[str] = None

