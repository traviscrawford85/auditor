# Adapter for servicetypeshow
from clio_sdk.models.servicetypeshow import ServicetypeshowIn, ServicetypeshowOut, ServicetypeshowUpdate, ServicetypeshowDb
from clio_client.models.service_type_show import ServiceTypeShow

def convert_sdk_to_servicetypeshowout(src: ServiceTypeShow) -> ServicetypeshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return ServicetypeshowOut(**src.model_dump())

def convert_servicetypeshowin_to_sdk(src: ServicetypeshowIn) -> ServiceTypeShow:
    """Converts a clio_sdk model to clio_client model."""
    return ServiceTypeShow(**src.model_dump())
