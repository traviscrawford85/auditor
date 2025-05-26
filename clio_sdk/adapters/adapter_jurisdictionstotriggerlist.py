# Adapter for jurisdictionstotriggerlist
from clio_sdk.models.jurisdictionstotriggerlist import JurisdictionstotriggerlistIn, JurisdictionstotriggerlistOut, JurisdictionstotriggerlistUpdate, JurisdictionstotriggerlistDb
from clio_client.models import jurisdictions_to_trigger_list

def convert_sdk_to_jurisdictionstotriggerlistout(src: jurisdictions_to_trigger_list) -> JurisdictionstotriggerlistOut:
    return JurisdictionstotriggerlistOut(**src.dict())

def convert_jurisdictionstotriggerlistin_to_sdk(src: JurisdictionstotriggerlistIn) -> jurisdictions_to_trigger_list:
    return jurisdictions_to_trigger_list(**src.dict())
