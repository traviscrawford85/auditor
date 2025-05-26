# Adapter for polymorphiccustomratebase
from clio_sdk.models.polymorphiccustomratebase import PolymorphiccustomratebaseIn, PolymorphiccustomratebaseOut, PolymorphiccustomratebaseUpdate, PolymorphiccustomratebaseDb
from clio_client.models import polymorphic_custom_rate_base

def convert_sdk_to_polymorphiccustomratebaseout(src: polymorphic_custom_rate_base) -> PolymorphiccustomratebaseOut:
    return PolymorphiccustomratebaseOut(**src.dict())

def convert_polymorphiccustomratebasein_to_sdk(src: PolymorphiccustomratebaseIn) -> polymorphic_custom_rate_base:
    return polymorphic_custom_rate_base(**src.dict())
