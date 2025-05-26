# Adapter for jurisdictionbase
from clio_sdk.models.jurisdictionbase import JurisdictionbaseIn, JurisdictionbaseOut, JurisdictionbaseUpdate, JurisdictionbaseDb
from clio_client.models import jurisdiction

def convert_sdk_to_jurisdictionbaseout(src: jurisdiction) -> JurisdictionbaseOut:
    return JurisdictionbaseOut(**src.dict())

def convert_jurisdictionbasein_to_sdk(src: JurisdictionbaseIn) -> jurisdiction:
    return jurisdiction(**src.dict())
