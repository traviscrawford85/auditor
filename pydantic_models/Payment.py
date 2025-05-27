from pydantic import BaseModel


class PaymentIn(BaseModel):
    """Incoming model for creating a Payment"""
    # TODO: Add fields


class PaymentOut(BaseModel):
    """Outgoing model for returning a Payment"""
    # TODO: Add fields


class PaymentUpdate(BaseModel):
    """Update model for patching a Payment"""
    # TODO: Add fields


class PaymentDb(BaseModel):
    """Internal DB representation for Payment"""
    # TODO: Add fields
