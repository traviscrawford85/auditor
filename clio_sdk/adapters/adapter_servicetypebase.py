# Adapter for servicetypebase
from clio_sdk.models.servicetypebase import ServicetypebaseIn, ServicetypebaseOut, ServicetypebaseUpdate, ServicetypebaseDb
from clio_client.models import service_type

def convert_sdk_to_servicetypebaseout(src: service_type) -> ServicetypebaseOut:
    return ServicetypebaseOut(**src.dict())

def convert_servicetypebasein_to_sdk(src: ServicetypebaseIn) -> service_type:
    return service_type(**src.dict())
