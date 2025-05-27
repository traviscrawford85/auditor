from pydantic import BaseModel


class CurrencyListIn(BaseModel):
    """Incoming model for creating a Currencylist"""
    # TODO: Add fields


class CurrencylistOut(BaseModel):
    """Outgoing model for returning a Currencylist"""
    # TODO: Add fields


class CurrencylistUpdate(BaseModel):
    """Update model for patching a Currencylist"""
    # TODO: Add fields


class CurrencylistDb(BaseModel):
    """Internal DB representation for Currencylist"""
    # TODO: Add fields
