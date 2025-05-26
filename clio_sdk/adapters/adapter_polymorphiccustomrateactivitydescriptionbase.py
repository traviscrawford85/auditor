# Adapter for polymorphiccustomrateactivitydescriptionbase
from clio_sdk.models.polymorphiccustomrateactivitydescriptionbase import PolymorphiccustomrateactivitydescriptionBaseIn, PolymorphiccustomrateactivitydescriptionbaseOut, PolymorphiccustomrateactivitydescriptionbaseUpdate, PolymorphiccustomrateactivitydescriptionbaseDb
from clio_client.models.polymorphic_custom_rate_activity_description_base import PolymorphicCustomRateActivityDescriptionBase

def convert_sdk_to_polymorphiccustomrateactivitydescriptionbaseout(src: PolymorphicCustomRateActivityDescriptionBase) -> PolymorphiccustomrateactivitydescriptionbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return PolymorphiccustomrateactivitydescriptionbaseOut(**src.model_dump())

def convert_polymorphiccustomrateactivitydescriptionbasein_to_sdk(src: PolymorphiccustomrateactivitydescriptionBaseIn) -> PolymorphicCustomRateActivityDescriptionBase:
    """Converts a clio_sdk model to clio_client model."""
    return PolymorphicCustomRateActivityDescriptionBase(**src.model_dump())
