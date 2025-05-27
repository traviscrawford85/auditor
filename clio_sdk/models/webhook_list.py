from typing import List

from pydantic import BaseModel

from .webhook import WebhookOut


class WebhookListIn(BaseModel):
    data: List[WebhookIn]

class WebhookListOut(BaseModel):
    data: List[WebhookOut]

class WebhookListUpdate(BaseModel):
    data: List[WebhookUpdate]

class WebhookListDb(BaseModel):
    data: List[WebhookDb]

