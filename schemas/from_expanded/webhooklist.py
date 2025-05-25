from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class WebhookListIn(BaseModel):
    data: List[Any]

class WebhookListOut(BaseModel):
    data: List[Any]

class WebhookListUpdate(BaseModel):
    data: List[Any]

class WebhookListDb(BaseModel):
    data: List[Any]

