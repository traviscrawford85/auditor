from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ClientShowIn(BaseModel):
    data: Any

class ClientShowOut(BaseModel):
    data: Any

class ClientShowUpdate(BaseModel):
    data: Any

class ClientShowDb(BaseModel):
    data: Any

