# Adapter for servicetypelist
from clio_sdk.models.servicetypelist import ServicetypelistIn, ServicetypelistOut, ServicetypelistUpdate, ServicetypelistDb
from clio_client.models.service_type_list import ServiceTypeList

def convert_sdk_to_servicetypelistout(src: ServiceTypeList) -> ServicetypelistOut:
    """Converts a clio_client model to clio_sdk model."""
    return ServicetypelistOut(**src.model_dump())

def convert_servicetypelistin_to_sdk(src: ServicetypelistIn) -> ServiceTypeList:
    """Converts a clio_sdk model to clio_client model."""
    return ServiceTypeList(**src.model_dump())
