from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime

class WebhookShowIn(BaseModel):
    data: Any

class WebhookShowOut(BaseModel):
    data: Any

class WebhookShowUpdate(BaseModel):
    data: Any

class WebhookShowDb(BaseModel):
    data: Any

