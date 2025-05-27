from pydantic import BaseModel


class BillrecipientIn(BaseModel):
    """Incoming model for creating a Billrecipient"""
    # TODO: Add fields


class BillrecipientOut(BaseModel):
    """Outgoing model for returning a Billrecipient"""
    # TODO: Add fields


class BillrecipientUpdate(BaseModel):
    """Update model for patching a Billrecipient"""
    # TODO: Add fields


class BillrecipientDb(BaseModel):
    """Internal DB representation for Billrecipient"""
    # TODO: Add fields
