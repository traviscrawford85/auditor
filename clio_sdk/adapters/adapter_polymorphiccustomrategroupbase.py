# Adapter for polymorphiccustomrategroupbase
from clio_sdk.models.polymorphiccustomrategroupbase import PolymorphiccustomrategroupBaseIn, PolymorphiccustomrategroupbaseOut, PolymorphiccustomrategroupbaseUpdate, PolymorphiccustomrategroupbaseDb
from clio_client.models.polymorphic_custom_rate_group_base import PolymorphicCustomRateGroupBase

def convert_sdk_to_polymorphiccustomrategroupbaseout(src: PolymorphicCustomRateGroupBase) -> PolymorphiccustomrategroupbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return PolymorphiccustomrategroupbaseOut(**src.model_dump())

def convert_polymorphiccustomrategroupbasein_to_sdk(src: PolymorphiccustomrategroupBaseIn) -> PolymorphicCustomRateGroupBase:
    """Converts a clio_sdk model to clio_client model."""
    return PolymorphicCustomRateGroupBase(**src.model_dump())
