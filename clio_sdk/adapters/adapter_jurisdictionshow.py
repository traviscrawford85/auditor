# Adapter for jurisdictionshow
from clio_sdk.models.jurisdictionshow import JurisdictionshowIn, JurisdictionshowOut, JurisdictionshowUpdate, JurisdictionshowDb
from clio_client.models.jurisdiction_show import JurisdictionShow

def convert_sdk_to_jurisdictionshowout(src: JurisdictionShow) -> JurisdictionshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return JurisdictionshowOut(**src.model_dump())

def convert_jurisdictionshowin_to_sdk(src: JurisdictionshowIn) -> JurisdictionShow:
    """Converts a clio_sdk model to clio_client model."""
    return JurisdictionShow(**src.model_dump())
