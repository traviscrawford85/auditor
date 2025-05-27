from pydantic import BaseModel


class DocumentIn(BaseModel):
    """Incoming model for creating a Document"""
    # TODO: Add fields


class DocumentOut(BaseModel):
    """Outgoing model for returning a Document"""
    # TODO: Add fields


class DocumentUpdate(BaseModel):
    """Update model for patching a Document"""
    # TODO: Add fields


class DocumentDb(BaseModel):
    """Internal DB representation for Document"""
    # TODO: Add fields
