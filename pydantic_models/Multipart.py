from pydantic import BaseModel


class MultipartIn(BaseModel):
    """Incoming model for creating a Multipart"""
    # TODO: Add fields


class MultipartOut(BaseModel):
    """Outgoing model for returning a Multipart"""
    # TODO: Add fields


class MultipartUpdate(BaseModel):
    """Update model for patching a Multipart"""
    # TODO: Add fields


class MultipartDb(BaseModel):
    """Internal DB representation for Multipart"""
    # TODO: Add fields
