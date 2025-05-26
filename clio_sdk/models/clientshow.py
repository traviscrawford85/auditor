from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class ClientShowIn(BaseModel):
    data: Client

class ClientShowOut(BaseModel):
    data: Client

class ClientShowUpdate(BaseModel):
    data: Client

class ClientShowDb(BaseModel):
    data: Client

