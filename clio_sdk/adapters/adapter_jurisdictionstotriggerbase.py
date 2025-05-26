# Adapter for jurisdictionstotriggerbase
from clio_sdk.models.jurisdictionstotriggerbase import JurisdictionstotriggerbaseIn, JurisdictionstotriggerbaseOut, JurisdictionstotriggerbaseUpdate, JurisdictionstotriggerbaseDb
from clio_client.models import jurisdictions_to_trigger

def convert_sdk_to_jurisdictionstotriggerbaseout(src: jurisdictions_to_trigger) -> JurisdictionstotriggerbaseOut:
    return JurisdictionstotriggerbaseOut(**src.dict())

def convert_jurisdictionstotriggerbasein_to_sdk(src: JurisdictionstotriggerbaseIn) -> jurisdictions_to_trigger:
    return jurisdictions_to_trigger(**src.dict())
