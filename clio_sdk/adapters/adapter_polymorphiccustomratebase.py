# Adapter for polymorphiccustomratebase
from clio_sdk.models.polymorphiccustomratebase import PolymorphiccustomrateBaseIn, PolymorphiccustomratebaseOut, PolymorphiccustomratebaseUpdate, PolymorphiccustomratebaseDb
from clio_client.models.polymorphic_custom_rate_base import PolymorphicCustomRateBase

def convert_sdk_to_polymorphiccustomratebaseout(src: PolymorphicCustomRateBase) -> PolymorphiccustomratebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return PolymorphiccustomratebaseOut(**src.model_dump())

def convert_polymorphiccustomratebasein_to_sdk(src: PolymorphiccustomrateBaseIn) -> PolymorphicCustomRateBase:
    """Converts a clio_sdk model to clio_client model."""
    return PolymorphicCustomRateBase(**src.model_dump())
