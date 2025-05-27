from pydantic import BaseModel


class ServicetypeShowIn(BaseModel):
    """Incoming model for creating a Servicetypeshow"""
    # TODO: Add fields


class ServicetypeshowOut(BaseModel):
    """Outgoing model for returning a Servicetypeshow"""
    # TODO: Add fields


class ServicetypeShowUpdate(BaseModel):
    """Update model for patching a Servicetypeshow"""
    # TODO: Add fields


class ServicetypeshowDb(BaseModel):
    """Internal DB representation for Servicetypeshow"""
    # TODO: Add fields
