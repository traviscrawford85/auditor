from typing import Optional

from pydantic import BaseModel


class ActivitycreaterequestdataclientportalIn(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdataclientportalOut(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdataclientportalUpdate(BaseModel):
    id: Optional[str] = None

class ActivitycreaterequestdataclientportalDb(BaseModel):
    id: Optional[str] = None

