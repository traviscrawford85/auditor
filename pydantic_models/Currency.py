from pydantic import BaseModel


class CurrencyIn(BaseModel):
    """Incoming model for creating a Currency"""
    # TODO: Add fields


class CurrencyOut(BaseModel):
    """Outgoing model for returning a Currency"""
    # TODO: Add fields


class CurrencyUpdate(BaseModel):
    """Update model for patching a Currency"""
    # TODO: Add fields


class CurrencyDb(BaseModel):
    """Internal DB representation for Currency"""
    # TODO: Add fields
