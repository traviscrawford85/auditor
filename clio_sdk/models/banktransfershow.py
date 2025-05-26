from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class BanktransferShowIn(BaseModel):
    data: Banktransfer

class BanktransferShowOut(BaseModel):
    data: Banktransfer

class BanktransferShowUpdate(BaseModel):
    data: Banktransfer

class BanktransferShowDb(BaseModel):
    data: Banktransfer

