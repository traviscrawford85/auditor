from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class MattercreaterequestdataclientIn(BaseModel):
    id: int

class MattercreaterequestdataclientOut(BaseModel):
    id: int

class MattercreaterequestdataclientUpdate(BaseModel):
    id: int

class MattercreaterequestdataclientDb(BaseModel):
    id: int

