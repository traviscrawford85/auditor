# Adapter for externalpropertybase
from clio_sdk.models.externalpropertybase import ExternalpropertybaseIn, ExternalpropertybaseOut, ExternalpropertybaseUpdate, ExternalpropertybaseDb
from clio_client.models import external_property_base

def convert_sdk_to_externalpropertybaseout(src: external_property_base) -> ExternalpropertybaseOut:
    return ExternalpropertybaseOut(**src.dict())

def convert_externalpropertybasein_to_sdk(src: ExternalpropertybaseIn) -> external_property_base:
    return external_property_base(**src.dict())
