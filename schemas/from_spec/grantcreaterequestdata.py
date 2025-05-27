from typing import Optional

from pydantic import BaseModel


class GrantcreaterequestdataIn(BaseModel):
    name: Optional[str] = None

class GrantcreaterequestdataOut(BaseModel):
    name: Optional[str] = None

class GrantcreaterequestdataUpdate(BaseModel):
    name: Optional[str] = None

class GrantcreaterequestdataDb(BaseModel):
    name: Optional[str] = None

