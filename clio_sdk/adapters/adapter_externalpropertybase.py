# Adapter for externalpropertybase
from clio_sdk.models.externalpropertybase import ExternalpropertyBaseIn, ExternalpropertybaseOut, ExternalpropertybaseUpdate, ExternalpropertybaseDb
from clio_client.models.external_property_base import ExternalPropertyBase

def convert_sdk_to_externalpropertybaseout(src: ExternalPropertyBase) -> ExternalpropertybaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ExternalpropertybaseOut(**src.model_dump())

def convert_externalpropertybasein_to_sdk(src: ExternalpropertyBaseIn) -> ExternalPropertyBase:
    """Converts a clio_sdk model to clio_client model."""
    return ExternalPropertyBase(**src.model_dump())
