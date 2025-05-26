# Adapter for jurisdictionstotriggerbase
from clio_sdk.models.jurisdictionstotriggerbase import JurisdictionstotriggerBaseIn, JurisdictionstotriggerbaseOut, JurisdictionstotriggerbaseUpdate, JurisdictionstotriggerbaseDb
from clio_client.models.jurisdictions_to_trigger import JurisdictionsToTrigger

def convert_sdk_to_jurisdictionstotriggerbaseout(src: JurisdictionsToTrigger) -> JurisdictionstotriggerbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return JurisdictionstotriggerbaseOut(**src.model_dump())

def convert_jurisdictionstotriggerbasein_to_sdk(src: JurisdictionstotriggerBaseIn) -> JurisdictionsToTrigger:
    """Converts a clio_sdk model to clio_client model."""
    return JurisdictionsToTrigger(**src.model_dump())
