# Adapter for webhookshow
from clio_sdk.models.webhookshow import WebhookshowIn, WebhookshowOut, WebhookshowUpdate, WebhookshowDb
from clio_client.models import webhook_show

def convert_sdk_to_webhookshowout(src: webhook_show) -> WebhookshowOut:
    return WebhookshowOut(**src.dict())

def convert_webhookshowin_to_sdk(src: WebhookshowIn) -> webhook_show:
    return webhook_show(**src.dict())
