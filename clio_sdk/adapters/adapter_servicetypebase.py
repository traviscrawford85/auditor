# Adapter for servicetypebase
from clio_sdk.models.servicetypebase import ServicetypeBaseIn, ServicetypebaseOut, ServicetypebaseUpdate, ServicetypebaseDb
from clio_client.models.service_type import ServiceType

def convert_sdk_to_servicetypebaseout(src: ServiceType) -> ServicetypebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ServicetypebaseOut(**src.model_dump())

def convert_servicetypebasein_to_sdk(src: ServicetypeBaseIn) -> ServiceType:
    """Converts a clio_sdk model to clio_client model."""
    return ServiceType(**src.model_dump())
