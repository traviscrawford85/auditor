# Adapter for jurisdictionlist
from clio_sdk.models.jurisdictionlist import JurisdictionlistIn, JurisdictionlistOut, JurisdictionlistUpdate, JurisdictionlistDb
from clio_client.models import jurisdiction_list

def convert_sdk_to_jurisdictionlistout(src: jurisdiction_list) -> JurisdictionlistOut:
    return JurisdictionlistOut(**src.dict())

def convert_jurisdictionlistin_to_sdk(src: JurisdictionlistIn) -> jurisdiction_list:
    return jurisdiction_list(**src.dict())
