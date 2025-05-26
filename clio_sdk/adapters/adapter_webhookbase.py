# Adapter for webhookbase
from clio_sdk.models.webhookbase import WebhookBaseIn, WebhookbaseOut, WebhookbaseUpdate, WebhookbaseDb
from clio_client.models.webhook import Webhook

def convert_sdk_to_webhookbaseout(src: Webhook) -> WebhookbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return WebhookbaseOut(**src.model_dump())

def convert_webhookbasein_to_sdk(src: WebhookBaseIn) -> Webhook:
    """Converts a clio_sdk model to clio_client model."""
    return Webhook(**src.model_dump())
