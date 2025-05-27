from typing import Optional

from pydantic import BaseModel


class GrantfundingsourcecreaterequestdataIn(BaseModel):
    name: Optional[str] = None

class GrantfundingsourcecreaterequestdataOut(BaseModel):
    name: Optional[str] = None

class GrantfundingsourcecreaterequestdataUpdate(BaseModel):
    name: Optional[str] = None

class GrantfundingsourcecreaterequestdataDb(BaseModel):
    name: Optional[str] = None

