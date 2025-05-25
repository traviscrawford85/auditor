from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ContactupdaterequestdataaddressesinnerIn(BaseModel):
    name: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

class ContactupdaterequestdataaddressesinnerOut(BaseModel):
    name: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

class ContactupdaterequestdataaddressesinnerUpdate(BaseModel):
    name: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

class ContactupdaterequestdataaddressesinnerDb(BaseModel):
    name: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    id: Optional[str] = None
    _destroy: Optional[str] = None

