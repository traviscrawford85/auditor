# Adapter for myeventbase
from clio_sdk.models.myeventbase import MyeventBaseIn, MyeventbaseOut, MyeventbaseUpdate, MyeventbaseDb
from clio_client.models.my_event import MyEvent

def convert_sdk_to_myeventbaseout(src: MyEvent) -> MyeventbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return MyeventbaseOut(**src.model_dump())

def convert_myeventbasein_to_sdk(src: MyeventBaseIn) -> MyEvent:
    """Converts a clio_sdk model to clio_client model."""
    return MyEvent(**src.model_dump())
