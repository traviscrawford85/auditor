# Adapter for jurisdictionshow
from clio_sdk.models.jurisdictionshow import JurisdictionshowIn, JurisdictionshowOut, JurisdictionshowUpdate, JurisdictionshowDb
from clio_client.models import jurisdiction_show

def convert_sdk_to_jurisdictionshowout(src: jurisdiction_show) -> JurisdictionshowOut:
    return JurisdictionshowOut(**src.dict())

def convert_jurisdictionshowin_to_sdk(src: JurisdictionshowIn) -> jurisdiction_show:
    return jurisdiction_show(**src.dict())
