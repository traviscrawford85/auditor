from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class WebhookShowIn(BaseModel):
    data: Webhook

class WebhookShowOut(BaseModel):
    data: Webhook

class WebhookShowUpdate(BaseModel):
    data: Webhook

class WebhookShowDb(BaseModel):
    data: Webhook

