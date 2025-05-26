# Adapter for webhookshow
from clio_sdk.models.webhookshow import WebhookshowIn, WebhookshowOut, WebhookshowUpdate, WebhookshowDb
from clio_client.models.webhook_show import WebhookShow

def convert_sdk_to_webhookshowout(src: WebhookShow) -> WebhookshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return WebhookshowOut(**src.model_dump())

def convert_webhookshowin_to_sdk(src: WebhookshowIn) -> WebhookShow:
    """Converts a clio_sdk model to clio_client model."""
    return WebhookShow(**src.model_dump())
