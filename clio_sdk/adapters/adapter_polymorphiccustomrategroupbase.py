# Adapter for polymorphiccustomrategroupbase
from clio_sdk.models.polymorphiccustomrategroupbase import PolymorphiccustomrategroupbaseIn, PolymorphiccustomrategroupbaseOut, PolymorphiccustomrategroupbaseUpdate, PolymorphiccustomrategroupbaseDb
from clio_client.models import polymorphic_custom_rate_group_base

def convert_sdk_to_polymorphiccustomrategroupbaseout(src: polymorphic_custom_rate_group_base) -> PolymorphiccustomrategroupbaseOut:
    return PolymorphiccustomrategroupbaseOut(**src.dict())

def convert_polymorphiccustomrategroupbasein_to_sdk(src: PolymorphiccustomrategroupbaseIn) -> polymorphic_custom_rate_group_base:
    return polymorphic_custom_rate_group_base(**src.dict())
