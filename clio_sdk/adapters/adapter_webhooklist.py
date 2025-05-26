# Adapter for webhooklist
from clio_sdk.models.webhooklist import WebhooklistIn, WebhooklistOut, WebhooklistUpdate, WebhooklistDb
from clio_client.models.webhook_list import WebhookList

def convert_sdk_to_webhooklistout(src: WebhookList) -> WebhooklistOut:
    """Converts a clio_client model to clio_sdk model."""
    return WebhooklistOut(**src.model_dump())

def convert_webhooklistin_to_sdk(src: WebhooklistIn) -> WebhookList:
    """Converts a clio_sdk model to clio_client model."""
    return WebhookList(**src.model_dump())
