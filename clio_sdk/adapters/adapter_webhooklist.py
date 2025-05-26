# Adapter for webhooklist
from clio_sdk.models.webhooklist import WebhooklistIn, WebhooklistOut, WebhooklistUpdate, WebhooklistDb
from clio_client.models import webhook_list

def convert_sdk_to_webhooklistout(src: webhook_list) -> WebhooklistOut:
    return WebhooklistOut(**src.dict())

def convert_webhooklistin_to_sdk(src: WebhooklistIn) -> webhook_list:
    return webhook_list(**src.dict())
