# Adapter for jurisdictionlist
from clio_sdk.models.jurisdictionlist import JurisdictionlistIn, JurisdictionlistOut, JurisdictionlistUpdate, JurisdictionlistDb
from clio_client.models.jurisdiction_list import JurisdictionList

def convert_sdk_to_jurisdictionlistout(src: JurisdictionList) -> JurisdictionlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return JurisdictionlistOut(**src.model_dump())

def convert_jurisdictionlistin_to_sdk(src: JurisdictionlistIn) -> JurisdictionList:
    """Converts a clio_sdk model to clio_client model."""
    return JurisdictionList(**src.model_dump())
