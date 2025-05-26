# Adapter for jurisdictionstotriggerlist
from clio_sdk.models.jurisdictionstotriggerlist import JurisdictionstotriggerlistIn, JurisdictionstotriggerlistOut, JurisdictionstotriggerlistUpdate, JurisdictionstotriggerlistDb
from clio_client.models.jurisdictions_to_trigger_list import JurisdictionsToTriggerList

def convert_sdk_to_jurisdictionstotriggerlistout(src: JurisdictionsToTriggerList) -> JurisdictionstotriggerlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return JurisdictionstotriggerlistOut(**src.model_dump())

def convert_jurisdictionstotriggerlistin_to_sdk(src: JurisdictionstotriggerlistIn) -> JurisdictionsToTriggerList:
    """Converts a clio_sdk model to clio_client model."""
    return JurisdictionsToTriggerList(**src.model_dump())
