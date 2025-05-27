from pydantic import BaseModel


class WebhookShowIn(BaseModel):
    """Incoming model for creating a Webhookshow"""
    # TODO: Add fields


class WebhookshowOut(BaseModel):
    """Outgoing model for returning a Webhookshow"""
    # TODO: Add fields


class WebhookShowUpdate(BaseModel):
    """Update model for patching a Webhookshow"""
    # TODO: Add fields


class WebhookshowDb(BaseModel):
    """Internal DB representation for Webhookshow"""
    # TODO: Add fields
