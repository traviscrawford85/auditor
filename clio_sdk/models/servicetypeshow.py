from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ServicetypeShowIn(BaseModel):
    data: Servicetype

class ServicetypeShowOut(BaseModel):
    data: Servicetype

class ServicetypeShowUpdate(BaseModel):
    data: Servicetype

class ServicetypeShowDb(BaseModel):
    data: Servicetype

