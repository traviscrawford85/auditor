# Adapter for polymorphiccustomrateuserbase
from clio_sdk.models.polymorphiccustomrateuserbase import PolymorphiccustomrateuserbaseIn, PolymorphiccustomrateuserbaseOut, PolymorphiccustomrateuserbaseUpdate, PolymorphiccustomrateuserbaseDb
from clio_client.models import polymorphic_custom_rate_base

def convert_sdk_to_polymorphiccustomrateuserbaseout(src: polymorphic_custom_rate_base) -> PolymorphiccustomrateuserbaseOut:
    return PolymorphiccustomrateuserbaseOut(**src.dict())

def convert_polymorphiccustomrateuserbasein_to_sdk(src: PolymorphiccustomrateuserbaseIn) -> polymorphic_custom_rate_base:
    return polymorphic_custom_rate_base(**src.dict())
