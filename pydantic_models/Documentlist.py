from pydantic import BaseModel


class DocumentListIn(BaseModel):
    """Incoming model for creating a Documentlist"""
    # TODO: Add fields


class DocumentlistOut(BaseModel):
    """Outgoing model for returning a Documentlist"""
    # TODO: Add fields


class DocumentlistUpdate(BaseModel):
    """Update model for patching a Documentlist"""
    # TODO: Add fields


class DocumentlistDb(BaseModel):
    """Internal DB representation for Documentlist"""
    # TODO: Add fields
