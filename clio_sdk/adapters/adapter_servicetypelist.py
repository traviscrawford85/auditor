# Adapter for servicetypelist
from clio_sdk.models.servicetypelist import ServicetypelistIn, ServicetypelistOut, ServicetypelistUpdate, ServicetypelistDb
from clio_client.models import service_type_list

def convert_sdk_to_servicetypelistout(src: service_type_list) -> ServicetypelistOut:
    return ServicetypelistOut(**src.dict())

def convert_servicetypelistin_to_sdk(src: ServicetypelistIn) -> service_type_list:
    return service_type_list(**src.dict())
