from typing import Optional

from pydantic import BaseModel


class CustomfieldcreaterequestdatapicklistoptionsinnerIn(BaseModel):
    id: Optional[str] = None
    option: Optional[str] = None
    _deleted: Optional[str] = None

class CustomfieldcreaterequestdatapicklistoptionsinnerOut(BaseModel):
    id: Optional[str] = None
    option: Optional[str] = None
    _deleted: Optional[str] = None

class CustomfieldcreaterequestdatapicklistoptionsinnerUpdate(BaseModel):
    id: Optional[str] = None
    option: Optional[str] = None
    _deleted: Optional[str] = None

class CustomfieldcreaterequestdatapicklistoptionsinnerDb(BaseModel):
    id: Optional[str] = None
    option: Optional[str] = None
    _deleted: Optional[str] = None

