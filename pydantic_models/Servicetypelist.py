from pydantic import BaseModel


class ServicetypeListIn(BaseModel):
    """Incoming model for creating a Servicetypelist"""
    # TODO: Add fields


class ServicetypelistOut(BaseModel):
    """Outgoing model for returning a Servicetypelist"""
    # TODO: Add fields


class ServicetypelistUpdate(BaseModel):
    """Update model for patching a Servicetypelist"""
    # TODO: Add fields


class ServicetypelistDb(BaseModel):
    """Internal DB representation for Servicetypelist"""
    # TODO: Add fields
