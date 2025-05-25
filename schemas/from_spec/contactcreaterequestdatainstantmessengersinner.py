from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ContactcreaterequestdatainstantmessengersinnerIn(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None

class ContactcreaterequestdatainstantmessengersinnerOut(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None

class ContactcreaterequestdatainstantmessengersinnerUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None

class ContactcreaterequestdatainstantmessengersinnerDb(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None

