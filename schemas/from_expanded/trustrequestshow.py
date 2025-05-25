from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class TrustrequestShowIn(BaseModel):
    data: Any

class TrustrequestShowOut(BaseModel):
    data: Any

class TrustrequestShowUpdate(BaseModel):
    data: Any

class TrustrequestShowDb(BaseModel):
    data: Any

