from pydantic import BaseModel


class DocumentShowIn(BaseModel):
    """Incoming model for creating a Documentshow"""
    # TODO: Add fields


class DocumentshowOut(BaseModel):
    """Outgoing model for returning a Documentshow"""
    # TODO: Add fields


class DocumentShowUpdate(BaseModel):
    """Update model for patching a Documentshow"""
    # TODO: Add fields


class DocumentshowDb(BaseModel):
    """Internal DB representation for Documentshow"""
    # TODO: Add fields
