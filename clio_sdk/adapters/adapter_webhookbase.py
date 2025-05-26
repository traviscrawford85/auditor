# Adapter for webhookbase
from clio_sdk.models.webhookbase import WebhookbaseIn, WebhookbaseOut, WebhookbaseUpdate, WebhookbaseDb
from clio_client.models import webhook

def convert_sdk_to_webhookbaseout(src: webhook) -> WebhookbaseOut:
    return WebhookbaseOut(**src.dict())

def convert_webhookbasein_to_sdk(src: WebhookbaseIn) -> webhook:
    return webhook(**src.dict())
