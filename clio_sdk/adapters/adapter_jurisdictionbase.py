# Adapter for jurisdictionbase
from clio_sdk.models.jurisdictionbase import JurisdictionBaseIn, JurisdictionbaseOut, JurisdictionbaseUpdate, JurisdictionbaseDb
from clio_client.models.jurisdiction import Jurisdiction

def convert_sdk_to_jurisdictionbaseout(src: Jurisdiction) -> JurisdictionbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return JurisdictionbaseOut(**src.model_dump())

def convert_jurisdictionbasein_to_sdk(src: JurisdictionBaseIn) -> Jurisdiction:
    """Converts a clio_sdk model to clio_client model."""
    return Jurisdiction(**src.model_dump())
