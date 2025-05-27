
from pydantic import BaseModel

from .webhook import WebhookOut


class WebhookShowIn(BaseModel):
    data: WebhookIn

class WebhookShowOut(BaseModel):
    data: WebhookOut

class WebhookShowUpdate(BaseModel):
    data: WebhookUpdate

class WebhookShowDb(BaseModel):
    data: WebhookDb

