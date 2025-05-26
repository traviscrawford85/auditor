# Adapter for instantmessengerbase
from clio_sdk.models.instantmessengerbase import InstantmessengerbaseIn, InstantmessengerbaseOut, InstantmessengerbaseUpdate, InstantmessengerbaseDb
from clio_client.models import instant_messenger_base

def convert_sdk_to_instantmessengerbaseout(src: instant_messenger_base) -> InstantmessengerbaseOut:
    return InstantmessengerbaseOut(**src.dict())

def convert_instantmessengerbasein_to_sdk(src: InstantmessengerbaseIn) -> instant_messenger_base:
    return instant_messenger_base(**src.dict())
