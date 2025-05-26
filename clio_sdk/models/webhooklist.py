from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class WebhookListIn(BaseModel):
    data: List[Webhook]

class WebhookListOut(BaseModel):
    data: List[Webhook]

class WebhookListUpdate(BaseModel):
    data: List[Webhook]

class WebhookListDb(BaseModel):
    data: List[Webhook]

