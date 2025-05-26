# Adapter for servicetypeshow
from clio_sdk.models.servicetypeshow import ServicetypeshowIn, ServicetypeshowOut, ServicetypeshowUpdate, ServicetypeshowDb
from clio_client.models import service_type_show

def convert_sdk_to_servicetypeshowout(src: service_type_show) -> ServicetypeshowOut:
    return ServicetypeshowOut(**src.dict())

def convert_servicetypeshowin_to_sdk(src: ServicetypeshowIn) -> service_type_show:
    return service_type_show(**src.dict())
