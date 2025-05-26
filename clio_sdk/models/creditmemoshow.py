from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class CreditmemoShowIn(BaseModel):
    data: Creditmemo

class CreditmemoShowOut(BaseModel):
    data: Creditmemo

class CreditmemoShowUpdate(BaseModel):
    data: Creditmemo

class CreditmemoShowDb(BaseModel):
    data: Creditmemo

