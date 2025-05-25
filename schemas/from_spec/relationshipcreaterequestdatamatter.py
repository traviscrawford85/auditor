from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class RelationshipcreaterequestdatamatterIn(BaseModel):
    id: Optional[str] = None

class RelationshipcreaterequestdatamatterOut(BaseModel):
    id: Optional[str] = None

class RelationshipcreaterequestdatamatterUpdate(BaseModel):
    id: Optional[str] = None

class RelationshipcreaterequestdatamatterDb(BaseModel):
    id: Optional[str] = None

