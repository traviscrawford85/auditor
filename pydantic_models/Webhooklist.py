from pydantic import BaseModel


class WebhookListIn(BaseModel):
    """Incoming model for creating a Webhooklist"""
    # TODO: Add fields


class WebhooklistOut(BaseModel):
    """Outgoing model for returning a Webhooklist"""
    # TODO: Add fields


class WebhooklistUpdate(BaseModel):
    """Update model for patching a Webhooklist"""
    # TODO: Add fields


class WebhooklistDb(BaseModel):
    """Internal DB representation for Webhooklist"""
    # TODO: Add fields
