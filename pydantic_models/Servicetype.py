from pydantic import BaseModel


class ServicetypeIn(BaseModel):
    """Incoming model for creating a Servicetype"""
    # TODO: Add fields


class ServicetypeOut(BaseModel):
    """Outgoing model for returning a Servicetype"""
    # TODO: Add fields


class ServicetypeUpdate(BaseModel):
    """Update model for patching a Servicetype"""
    # TODO: Add fields


class ServicetypeDb(BaseModel):
    """Internal DB representation for Servicetype"""
    # TODO: Add fields
