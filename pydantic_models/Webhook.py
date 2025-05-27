from pydantic import BaseModel


class WebhookIn(BaseModel):
    """Incoming model for creating a Webhook"""
    # TODO: Add fields


class WebhookOut(BaseModel):
    """Outgoing model for returning a Webhook"""
    # TODO: Add fields


class WebhookUpdate(BaseModel):
    """Update model for patching a Webhook"""
    # TODO: Add fields


class WebhookDb(BaseModel):
    """Internal DB representation for Webhook"""
    # TODO: Add fields
