# Adapter for polymorphiccustomrateuserbase
from clio_sdk.models.polymorphiccustomrateuserbase import PolymorphiccustomrateuserBaseIn, PolymorphiccustomrateuserbaseOut, PolymorphiccustomrateuserbaseUpdate, PolymorphiccustomrateuserbaseDb
from clio_client.models.polymorphic_custom_rate_base import PolymorphicCustomRateBase

def convert_sdk_to_polymorphiccustomrateuserbaseout(src: PolymorphicCustomRateBase) -> PolymorphiccustomrateuserbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return PolymorphiccustomrateuserbaseOut(**src.model_dump())

def convert_polymorphiccustomrateuserbasein_to_sdk(src: PolymorphiccustomrateuserBaseIn) -> PolymorphicCustomRateBase:
    """Converts a clio_sdk model to clio_client model."""
    return PolymorphicCustomRateBase(**src.model_dump())
