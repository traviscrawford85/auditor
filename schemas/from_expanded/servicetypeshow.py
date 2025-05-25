from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ServicetypeShowIn(BaseModel):
    data: Any

class ServicetypeShowOut(BaseModel):
    data: Any

class ServicetypeShowUpdate(BaseModel):
    data: Any

class ServicetypeShowDb(BaseModel):
    data: Any

