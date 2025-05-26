# Adapter for instantmessengerbase
from clio_sdk.models.instantmessengerbase import InstantmessengerBaseIn, InstantmessengerbaseOut, InstantmessengerbaseUpdate, InstantmessengerbaseDb
from clio_client.models.instant_messenger_base import InstantMessengerBase

def convert_sdk_to_instantmessengerbaseout(src: InstantMessengerBase) -> InstantmessengerbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return InstantmessengerbaseOut(**src.model_dump())

def convert_instantmessengerbasein_to_sdk(src: InstantmessengerBaseIn) -> InstantMessengerBase:
    """Converts a clio_sdk model to clio_client model."""
    return InstantMessengerBase(**src.model_dump())
